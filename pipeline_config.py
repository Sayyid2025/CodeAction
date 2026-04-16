from dataclasses import dataclass

@dataclass
class VideoAnalysisPipelineConfig:
    """Configuration for the video analysis pipeline."""
    frame_skip: int  # Number of frames to skip
    yolo_every_n: int  # Run YOLO every n frames
    action_clip_len: int  # Length of action clip
    action_interval: int  # Interval for action processing
    max_grip_px: int  # Maximum grip size in pixels
    min_grip_px: int  # Minimum grip size in pixels
    save_output_video: bool  # Whether to save the output video
    show_visualization: bool  # Whether to show visualizations
    device: str  # Device to use ('cpu' or 'cuda')