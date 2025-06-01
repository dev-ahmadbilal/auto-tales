from pydantic import BaseModel
from crewai.flow import Flow, start, listen

from auto_tales.crews.production_crew.production_crew import ProductionCrew


class StoryState(BaseModel):
    story_idea: str = ""
    final_video_path: str = ""
    user_feedback: str = ""
    revised_tasks: str = ""


class ProductionFlow(Flow[StoryState]):
    
    @start()
    def get_story_idea(self):
        print("\n🎬 Welcome to AutoTales Story Creator!")
        print("Let's start by writing a story for kids aged 5 to 10.")
        print("Please enter a fun, moral, and simple story idea (no magic or philosophy).")
        self.state.story_idea = input("Story idea: ").strip()
        return self.state

    @listen(get_story_idea)
    def run_story_production(self):
        print("\n🛠 Running the full story production pipeline...")
        result = (
            ProductionCrew()
            .crew()
            .kickoff(inputs={"story_idea": self.state.story_idea})
        )

        # Save result to state (assuming result.raw contains video path)
        self.state.final_video_path = result.raw if isinstance(result.raw, str) else "output/final_video.mp4"
        print(f"\n✅ Story video generated! Check: {self.state.final_video_path}")

    # @listen(run_story_production)
    # def ask_for_feedback(self):
    #     print("\n📝 We'd love your feedback!")
    #     self.state.user_feedback = input("What did you think of the video? Any improvements? ").strip()

    #     # Save feedback
    #     with open("output/feedback.txt", "w") as f:
    #         f.write(self.state.user_feedback)

    #     print("✅ Feedback saved to output/feedback.txt")

    #     # Optionally re-kick based on feedback
    #     rerun = input("Would you like to revise based on this feedback? (yes/no): ").strip().lower()
    #     if rerun == "yes":
    #         print("🔁 Triggering feedback_processor task to revise workflow...")
    #         # In a real system, call FeedbackProcessor directly or rerun part of the crew
    #     else:
    #         print("🎉 Flow complete! Thanks for using AutoTales.")


def kickoff():
    production_flow = ProductionFlow()
    production_flow.kickoff()


def plot():
    production_flow = ProductionFlow()
    production_flow.plot()


if __name__ == "__main__":
    kickoff()