# Dataframe-AI

Dataframe-AI is a python library built on top of pandas to make data analysis and visualization easier. This is done by using the Generative capabilities of Large Language Models to generate code for us with just natural language instructions from the user.

NOTE: This is a work in progress and is not ready for use yet.

NOTE: This work is not a replacement for pandas, but rather a tool to make it easier to use pandas.

## Installation
```bash
pip install dataframe-ai
```

## Usage

### Generate API_KEY
Firstly, you need to get an API_KEY. Currently, we only support OPENAI LLMs. You can generate an API_KEY from [here](https://platform.openai.com/account/api-keys).

### Pass API_KEY as environment variable
After you have generated the API_KEY, you have to pass it as an environment variable. This can be done by:
```bash
cp .env.template .env
```
Now, add your API_KEY to the .env file.

### Use LLM to generate code
```python
import pandas as pd
import dataframe_ai as dfai

# Load the data
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])

# Instatiate LLM
from dfai.llm.openai import OpenAI
llm = OpenAI()

# Generate code
dataframe_ai = dfai.use_llm(llm)
dataframe_ai.generate_code(df, query="Sort the dataframe by age in descending order")
```

The above code will generate the following code:
```python
df.sort_values(by=['Age'], ascending=False)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
MIT License
