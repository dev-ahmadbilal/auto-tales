import os
from typing import List
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from auto_tales.crews.production_crew.types.schemas import CastList, FinalVideo, RevisionList, SceneEmotions, SceneList, Script, Story, VideoSegmentList, VoiceoverList
from auto_tales.tools.llm_provider import get_llm

@CrewBase
class ProductionCrew:
    """ProductionCrew: Automated children's storytelling and animation production."""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # === Agents ===
    @agent
    def StoryWriter(self) -> Agent:
        return Agent(
            config=self.agents_config["StoryWriter"],
            llm=get_llm(),
        )

    @agent
    def ScriptWriter(self) -> Agent:
        return Agent(
            config=self.agents_config["ScriptWriter"],
            llm=get_llm(),
        )

    @agent
    def SceneSplitter(self) -> Agent:
        return Agent(
            config=self.agents_config["SceneSplitter"],
            llm=get_llm(),
        )

    @agent
    def EmotionExtractor(self) -> Agent:
        return Agent(
            config=self.agents_config["EmotionExtractor"],
            llm=get_llm(),
        )

    @agent
    def CastPlanner(self) -> Agent:
        return Agent(
            config=self.agents_config["CastPlanner"],
            llm=get_llm(),
        )

    @agent
    def VoiceoverGenerator(self) -> Agent:
        return Agent(
            config=self.agents_config["VoiceoverGenerator"],
            llm=get_llm(),
        )

    @agent
    def VideoSynthesizer(self) -> Agent:
        return Agent(
            config=self.agents_config["VideoSynthesizer"],
            llm=get_llm(),
        )

    @agent
    def FinalAssembler(self) -> Agent:
        return Agent(
            config=self.agents_config["FinalAssembler"],
            llm=get_llm(),
        )

    @agent
    def FeedbackProcessor(self) -> Agent:
        return Agent(
            config=self.agents_config["FeedbackProcessor"],
            llm=get_llm(),
        )

    # === Tasks ===
    @task
    def story_writing(self) -> Task:
        return Task(
            config=self.tasks_config["story_writing"],
            output_json=Story 
        )

    @task
    def script_writing(self) -> Task:
        return Task(
            config=self.tasks_config["script_writing"],
            output_schema=Script
        )

    @task
    def scene_splitting(self) -> Task:
        return Task(
            config=self.tasks_config["scene_splitting"],
            output_schema=SceneList
        )

    @task
    def emotion_extraction(self) -> Task:
        return Task(
            config=self.tasks_config["emotion_extraction"],
            output_schema=SceneEmotions
        )

    @task
    def cast_planning(self) -> Task:
        return Task(
            config=self.tasks_config["cast_planning"],
            output_schema=CastList
        )

    @task
    def voiceover_generation(self) -> Task:
        return Task(
            config=self.tasks_config["voiceover_generation"],
            output_schema=VoiceoverList
        )

    @task
    def video_synthesis(self) -> Task:
        return Task(
            config=self.tasks_config["video_synthesis"],
            output_schema=VideoSegmentList
        )

    @task
    def final_assembly(self) -> Task:
        return Task(
            config=self.tasks_config["final_assembly"],
            output_schema=FinalVideo
        )

    @task
    def feedback_processing(self) -> Task:
        return Task(
            config=self.tasks_config["feedback_processing"],
            output_schema=RevisionList
        )

    # === Crew ===
    @crew
    def crew(self) -> Crew:
        """Creates the complete storytelling production crew."""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )