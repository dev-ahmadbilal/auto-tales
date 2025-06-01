from typing import List, Optional
from pydantic import BaseModel


class Story(BaseModel):
    full_story: str


class Script(BaseModel):
    script: str


class Scene(BaseModel):
    scene_id: str
    title: str
    location: str
    time_of_day: str
    summary: str
    content: str


class SceneList(BaseModel):
    scenes: List[Scene]


class EmotionEntry(BaseModel):
    scene_id: str
    character: str
    emotion: str
    voice_tone: str
    facial_expression: str
    body_language: str


class SceneEmotions(BaseModel):
    scene_emotions: List[EmotionEntry]


class CastMember(BaseModel):
    character: str
    persona: str
    age: str
    gender: str
    visual_identity: str
    vocal_profile: str


class CastList(BaseModel):
    cast_profiles: List[CastMember]


class VoiceoverEntry(BaseModel):
    scene_id: str
    character: str
    voice_clip: str  # Path or URL
    transcript: str


class VoiceoverList(BaseModel):
    voiceover: List[VoiceoverEntry]


class VideoSegment(BaseModel):
    scene_id: str
    video_clip: str  # Path or URL


class VideoSegmentList(BaseModel):
    video_segments: List[VideoSegment]


class FinalVideo(BaseModel):
    final_video: str  # Path or URL


class FeedbackRevision(BaseModel):
    task_name: str
    reason: str
    suggested_improvement: str


class RevisionList(BaseModel):
    revised_task_list: List[FeedbackRevision]