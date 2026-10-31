# Video Trimmer - Replicate Cog Model

A simple and efficient video trimming tool built as a Replicate Cog model. Perfect for content creators who need to quickly trim videos without complex editing software.

## Features

- **Flexible Trimming**: Trim from start, end, or specify duration
- **Multiple Formats**: Support for MP4, MOV, AVI, MKV, and WebM
- **Quality Control**: Choose encoding speed presets from ultrafast to veryslow
- **Audio Control**: Adjust volume or remove audio completely
- **Simple Interface**: Minimal parameters focused on core trimming functionality

## Usage

### Basic Trimming Examples

#### Remove First 2 Seconds
```json
{
  "video": "your-video.mp4",
  "start_time": "00:00:02"
}
```

#### Keep Only First 30 Seconds  
```json
{
  "video": "your-video.mp4",
  "end_time": "00:00:30"
}
```

#### Trim Middle Portion (10s to 45s)
```json
{
  "video": "your-video.mp4", 
  "start_time": "00:00:10",
  "end_time": "00:00:45"
}
```

#### Trim by Duration (5 minutes from start)
```json
{
  "video": "your-video.mp4",
  "start_time": "00:00:10", 
  "duration": "00:05:00"
}
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `video` | Path | *required* | Input video file to trim |
| `start_time` | string | `"00:00:00"` | Start time (HH:MM:SS, MM:SS, or seconds) |
| `end_time` | string | `null` | End time (HH:MM:SS, MM:SS, or seconds) |
| `duration` | string | `null` | Duration from start time (HH:MM:SS, MM:SS, or seconds) |
| `output_format` | string | `"mp4"` | Output format: mp4, mov, avi, mkv, webm |
| `quality` | string | `"medium"` | Encoding preset: ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow |
| `volume` | float | `1.0` | Audio volume multiplier (0.0 to 5.0) |
| `remove_audio` | boolean | `false` | Remove audio track completely |

## Time Format Examples

The model accepts flexible time formats:

- **HH:MM:SS**: `"01:23:45"` (1 hour, 23 minutes, 45 seconds)
- **MM:SS**: `"05:30"` (5 minutes, 30 seconds)  
- **Seconds**: `"90"` (90 seconds)

## Common Use Cases

### Content Creator Workflows

**Trim Intro/Outro**
```json
{
  "video": "raw-footage.mp4",
  "start_time": "00:00:05",
  "end_time": "00:12:30"
}
```

**Extract Highlight Clip**
```json
{
  "video": "full-stream.mp4",
  "start_time": "01:45:20", 
  "duration": "00:01:15",
  "output_format": "mp4"
}
```

**Create Silent Version**
```json
{
  "video": "original.mp4",
  "remove_audio": true
}
```

**Boost Audio for Quiet Video**
```json
{
  "video": "quiet-video.mp4",
  "volume": 2.0
}
```

## Technical Details

- **Video Codec**: H.264 (libx264) for broad compatibility
- **Audio Codec**: AAC at 128k bitrate (when audio included)
- **Processing**: Uses FFmpeg for reliable video processing
- **Temporary Files**: Automatically cleaned up after processing

## Quality Presets

| Preset | Speed | File Size | Use Case |
|--------|-------|-----------|----------|
| `ultrafast` | Fastest | Largest | Quick previews |
| `superfast` | Very Fast | Large | Draft exports |
| `veryfast` | Fast | Medium-Large | Standard workflow |
| `faster` | Fast | Medium | Balanced processing |
| `fast` | Moderate | Medium | Good quality/speed |
| `medium` | Moderate | Balanced | **Default - recommended** |
| `slow` | Slow | Small | High quality exports |
| `slower` | Very Slow | Smaller | Premium quality |
| `veryslow` | Slowest | Smallest | Maximum quality |

## Error Handling

The model validates inputs and provides clear error messages:

- At least one timing parameter must be specified
- Invalid time formats are rejected
- FFmpeg errors are captured and reported
- Temporary files are automatically cleaned up

## Deployment

This model is designed to run on Replicate. To deploy:

1. Ensure you have the Cog CLI installed
2. Run `cog predict` for local testing
3. Use `cog push` to deploy to Replicate

## Requirements

- FFmpeg (included in Cog environment)
- Python 3.8+
- Cog framework

## License

The code in this repository is licensed under the [Apache License 2.0](LICENSE).
