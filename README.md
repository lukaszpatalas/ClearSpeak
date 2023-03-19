# ClearSpeak

## Design 
ClearSpeak is an app with an easy-to-use visual interface that helps users convert industry-specific language into simpler terms that can be understood by people who aren't familiar with the technical terms, making it helpful for both customers and coworkers from different departments.

## Features
- Transforms technical work-related text into easily understandable language
- Suitable for various industries and departments
- User-friendly visual interface
- Offers two modes: natural and creative

## Tasks to do
- Check if there is any way to include AI-generated images (DALEE, MidJourney).
- Develop an app.
- Write benefits and significance of clear communication
- Prepare final version of README.md
- Explore options of recreating app in Power Apps, as it appears to utilize the GPT-4 model, but requires further confirmation.
- Explore options for moving the Python version to Azure.

## Extra ideas to explore
- Translation to multiple languages
- Speech-to-Text-Conversion (by utilizing Whisper)
- Integration with Instant Messaging Apps used by company
- Machine Learning-Powered Suggestions
- Cloud-Based Storage and Syncing

## Prompts

### Natural mode
Please rephrase the original text so that it is easily understood by both customers and non-technical departments while maintaining the original meaning and message. This will help ensure clear communication. Use natural language. Here is the original text:

### Creative mode
Please rephrase the original text so that it is easily understood by both customers and non-technical departments while maintaining the original meaning and message. This will help ensure clear communication. Use very creative language. Here is the original text:

## Example

| Type      | Text                                                                                                                                                    |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Original  | The exclusion criteria considered are: The metadata provides sufficient evidence that the study is not related to web development or engineering methodologies. The summary does not provide sufficient information or evidence to indicate that the research does not have an approach related to web application development methodologies. |
| Natural   | The factors used to exclude certain studies are: The study's background information clearly shows it's not related to website creation or engineering techniques. The study's summary doesn't give enough details or proof to show that the research isn't connected to methods used in developing web applications.                          |
| Creative  | The whimsical rules for leaving out certain studies include: The study's magical metadata unveils enough clues to show that it's not entwined with the art of web creation or the labyrinth of engineering tactics. The study's enchanting overview doesn't possess the necessary keys or tokens to reveal that the research isn't linked to the mystical realm of web application crafting methods.   |

## Getting Started (EXPAND on this)
These instructions will guide you on how to set up ClearSpeak on your local machine for development and testing purposes.

## AI Model
ClearSpeak currently uses the GPT-3.5-turbo model for text rewriting tasks. However, our goal is to upgrade to the GPT-4 Turbo model (once the API key becomes available) to enhance performance and capabilities.

### Why upgrade to GPT-4 Turbo?
GPT-4 Turbo outperforms GPT-3.5-turbo in aspects such as reliability, creativity, and handling complex instructions. GPT-4 is great at various tasks, like solving problems, answering multiple-choice questions, and assisting with languages that don't have many resources. This makes GPT-4 an ideal choice for the ClearSpeak app, as it will optimize the text rewriting process and produce more precise and creative outcomes.

### Comparison between gpt3.5 and gpt-4 models

![image](https://user-images.githubusercontent.com/106703426/226074988-aa426a3a-4762-4175-a1f0-f8edb8e5291e.png)
