from cog import BasePredictor, Input, Path
import os
import subprocess
import tempfile
from typing import Optional

class Predictor(BasePredictor):
    def predict(
        self,
        video: Path = Input(description="Input video file to trim"),
        start_time: str = Input(
            description="Start time for trimming (format: HH:MM:SS or MM:SS or seconds)", 
            default="00:00:00"
        ),
        end_time: Optional[str] = Input(
            description="End time for trimming (format: HH:MM:SS or MM:SS or seconds). If not specified, uses duration instead.",
            default=None
        ),
        duration: Optional[str] = Input(
            description="Duration to trim from start time (format: HH:MM:SS or MM:SS or seconds). Ignored if end_time is specified.",
            default=None
        ),
        output_format: str = Input(
            description="Output video format",
            choices=["mp4", "mov", "avi", "mkv", "webm"],
            default="mp4"
        ),
        quality: str = Input(
            description="Video quality preset",
            choices=["ultrafast", "superfast", "veryfast", "faster", "fast", "medium", "slow", "slower", "veryslow"],
            default="medium"
        ),
        remove_audio: bool = Input(
            description="Remove audio track from output video",
            default=False
        )
    ) -> Path:
        """
        Trim and process video with various options for content creators
        """
        
        # Validate inputs - now more flexible to allow trimming from start-to-end or beginning-to-end
        if not end_time and not duration and start_time == "00:00:00":
            raise ValueError("At least one of start_time, end_time, or duration must be specified")
        
        # Create temporary output file
        with tempfile.NamedTemporaryFile(suffix=f'.{output_format}', delete=False) as tmp_file:
            output_path = tmp_file.name
        
        try:
            # Build ffmpeg command
            cmd = ['ffmpeg', '-i', str(video), '-y']
            
            # Add start time
            if start_time != "00:00:00":
                cmd.extend(['-ss', start_time])
            
            # Add duration or end time
            if end_time:
                cmd.extend(['-to', end_time])
            elif duration:
                cmd.extend(['-t', duration])
            
            # Video codec settings
            cmd.extend(['-c:v', 'libx264', '-preset', quality])
            
            # Audio codec settings
            if remove_audio:
                cmd.extend(['-an'])
            else:
                cmd.extend(['-c:a', 'aac', '-b:a', '128k'])
            
            # Output file
            cmd.append(output_path)
            
            # Run ffmpeg command
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                raise RuntimeError(f"FFmpeg error: {result.stderr}")
            
            return Path(output_path)
            
        except Exception as e:
            # Clean up temporary file if there was an error
            if os.path.exists(output_path):
                os.unlink(output_path)
            raise e