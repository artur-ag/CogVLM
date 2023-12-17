import base64
from io import BytesIO
from PIL import Image

def images_are_same(img1: Image, img2: Image) -> bool:
    """
        Compare two PIL images.
    """
    if img1.size != img2.size or img1.mode != img2.mode:
        return False
    return list(img1.getdata()) == list(img2.getdata())


def encode_file_to_base64(file):
    """
       Convert a file to base64.
    """
    buffer = BytesIO()
    buffer.write(file.read())
    return base64.b64encode(buffer.getvalue()).decode()


# The templates is for CogAgent

templates = [
    "Can you advise me on how to <TASK>?",
    "I'm looking for guidance on how to <TASK>.",
    "What steps do I need to take to <TASK>?",
    "Could you provide instructions for <TASK>?",
    "I'm wondering what the process is for <TASK>.",
    "How can I go about <TASK>?",
    "I need assistance with planning to <TASK>.",
    "Do you have any recommendations for <TASK>?",
    "Please share some tips for <TASK>.",
    "I'd like to know the best way to <TASK>.",
    "What's the most effective way to <TASK>?",
    "I'm seeking advice on accomplishing <TASK>.",
    "Could you guide me through the steps to <TASK>?",
    "I'm unsure how to start with <TASK>.",
    "Is there a strategy for successfully <TASK>?",
    "What's the proper procedure for <TASK>?",
    "How should I prepare for <TASK>?",
    "I'm not sure where to begin with <TASK>.",
    "I need some insights on <TASK>.",
    "Can you explain how to tackle <TASK>?",
    "I'm interested in the process of <TASK>.",
    "Could you enlighten me on <TASK>?",
    "What are the recommended steps for <TASK>?",
    "Is there a preferred method for <TASK>?",
    "I'd appreciate your advice on <TASK>.",
    "Can you shed light on <TASK>?",
    "What would be the best approach to <TASK>?",
    "How do I get started with <TASK>?",
    "I'm inquiring about the procedure for <TASK>.",
    "Could you share your expertise on <TASK>?",
    "I'd like some guidance on <TASK>.",
    "What's your recommendation for <TASK>?",
    "I'm seeking your input on how to <TASK>.",
    "Can you provide some insights into <TASK>?",
    "How can I successfully accomplish <TASK>?",
    "What steps are involved in <TASK>?",
    "I'm curious about the best way to <TASK>.",
    "Could you show me the ropes for <TASK>?",
    "I need to know how to go about <TASK>.",
    "What are the essential steps for <TASK>?",
    "Is there a specific method for <TASK>?",
    "I'd like to get some advice on <TASK>.",
    "Can you explain the process of <TASK>?",
    "I'm looking for guidance on how to approach <TASK>.",
    "What's the proper way to handle <TASK>?",
    "How should I proceed with <TASK>?",
    "I'm interested in your expertise on <TASK>.",
    "Could you walk me through the steps for <TASK>?",
    "I'm not sure where to begin when it comes to <TASK>.",
    "What should I prioritize when doing <TASK>?",
    "How can I ensure success with <TASK>?",
    "I'd appreciate some tips on <TASK>.",
    "Can you provide a roadmap for <TASK>?",
    "What's the recommended course of action for <TASK>?",
    "I'm seeking your guidance on <TASK>.",
    "Could you offer some suggestions for <TASK>?",
    "I'd like to know the steps to take for <TASK>.",
    "What's the most effective way to achieve <TASK>?",
    "How can I make the most of <TASK>?",
    "I'm wondering about the best approach to <TASK>.",
    "Can you share your insights on <TASK>?",
    "What steps should I follow to complete <TASK>?",
    "I'm looking for advice on <TASK>.",
    "What's the strategy for successfully completing <TASK>?",
    "How should I prepare myself for <TASK>?",
    "I'm not sure where to start with <TASK>.",
    "What's the procedure for <TASK>?",
    "Could you provide some guidance on <TASK>?",
    "I'd like to get some tips on how to <TASK>.",
    "Can you explain how to tackle <TASK> step by step?",
    "I'm interested in understanding the process of <TASK>.",
    "What are the key steps to <TASK>?",
    "Is there a specific method that works for <TASK>?",
    "I'd appreciate your advice on successfully completing <TASK>.",
    "Can you shed light on the best way to <TASK>?",
    "What would you recommend as the first step to <TASK>?",
    "How do I initiate <TASK>?",
    "I'm inquiring about the recommended steps for <TASK>.",
    "Could you share some insights into <TASK>?",
    "I'm seeking your expertise on <TASK>.",
    "What's your recommended approach for <TASK>?",
    "I'd like some guidance on where to start with <TASK>.",
    "Can you provide recommendations for <TASK>?",
    "What's your advice for someone looking to <TASK>?",
    "I'm seeking your input on the process of <TASK>.",
    "How can I achieve success with <TASK>?",
    "What's the best way to navigate <TASK>?",
    "I'm curious about the steps required for <TASK>.",
    "Could you show me the proper way to <TASK>?",
    "I need to know the necessary steps for <TASK>.",
    "What's the most efficient method for <TASK>?",
    "I'd appreciate your guidance on <TASK>.",
    "Can you explain the steps involved in <TASK>?",
    "I'm looking for recommendations on how to approach <TASK>.",
    "What's the right way to handle <TASK>?",
    "How should I manage <TASK>?",
    "I'm interested in your insights on <TASK>.",
    "Could you provide a step-by-step guide for <TASK>?",
    "I'm not sure how to start when it comes to <TASK>.",
    "What are the key factors to consider for <TASK>?",
    "How can I ensure a successful outcome with <TASK>?",
    "I'd like some tips and tricks for <TASK>.",
    "Can you offer a roadmap for accomplishing <TASK>?",
    "What's the preferred course of action for <TASK>?",
    "I'm seeking your expert advice on <TASK>.",
    "Could you suggest some best practices for <TASK>?",
    "I'd like to understand the necessary steps to complete <TASK>.",
    "What's the most effective strategy for <TASK>?",
]
