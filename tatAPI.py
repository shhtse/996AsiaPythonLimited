import openai  # openAI ChatGPT
import config as cf # Bearer token
from textwrap import wrap
import datetime
from IPython.core.display import display, HTML

def chatToTat(prompt):
    completion = openai.ChatCompletion.create(
      model = 'gpt-3.5-turbo',
      messages=[{"role": "system", "content":"I am Tat Gor, a predictor system in 2200. You can ask me anything, and I will answer you all I know"},
            {'role': 'user', 'content': prompt}],
      temperature = 0.9, 
    )

    
    # Ask from user
    prompt = wrap(prompt, 80)
    display(HTML(f'<h2 style="display:flex;justify-content: flex-end;"><l>User</l></h2>'))
    display(HTML('<div></div>')
    display(HTML(f'<p style="display:flex;justify-content: flex-end;">{prompt[0]}<p/>'))
    ct = datetime.datetime.now()
    display(HTML(f'<p style="display:flex;justify-content: flex-end;">Replied time : {ct}<p/>'))
    display(HTML('<hr/>'))
    
    # reply from AI
    role = completion.choices[0]['message']['role']
    reply = completion.choices[0]['message']['content']
    result = wrap(reply, 70)
    display(HTML(f'<h2 style="color:rgb(60,115,168)"><l>{role.capitalize()}</l></h2>'))
    display(HTML('<div></div>')
    display(HTML(f'<p style="color:rgb(60,115,168)">{reply}<p/>'))
    ct = datetime.datetime.now()
    display(HTML(f'<p style="color:rgb(60,115,168)">Replied time : {ct}<p/>'))