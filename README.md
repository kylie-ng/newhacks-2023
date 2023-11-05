# newhacks-2023

Looking to push the boundaries of accessible education, introducing **Baby AI**

Baby AI is a GPT-powered educational aid that creates customized problem sets for all your courses!

Just provide a PDF of your class notes and Baby will generate you a problem set in no time! 

## How does it work?

Baby AI currently uses GPT-3.5-Turbo to power its problem set generation. Each PDF is parsed and its text is extracted, before being supplied to GPT as a prompt. The system prompt is set up as follows:

```
You are a problem set writer. Given a set of class notes, compile a problem set based on the relevant content. 
The output must be in GFM format so it can be easily exported as a PDF file. 
The conversion will happen through Pandoc, ensure no text overflows.
Show the problem set at the top, and the solution set at the bottom.
The problem set must contain {num_mcq} multiple choice questions and {num_long} long answer questions.
```