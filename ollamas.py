"""
This module provides functions to classify items as productive or unproductive and to generate analysis reports
based on application and website usage statistics.
"""
import logging

import ollama
import re

def get_classified_items(items):
    prompt = """
    You are my personal assistant who tries to classify whether this 'software application title' or 'browser web page domain'
    is 'productive' or 'unproductive'.
    
    You will be given a CSV list.
    
    - Classify any given 'software application title' or 'browser web page domain' provided
    in the input as 'unproductive' if the item is primarily a social media platform or communication tool known for
    promoting compare-with-friends behavior and lacking productivity features,
    Only classify similar applications/domain that do not have notable productivity tools despite being widely used on mobile
    devices. The classification should be based solely on the app/domain name without considering other data sources
    - Classify input as 'productive' if item related to work, study, or self-improvement.
    
    Output exactly and only the same list in CSV format. Do not add header to the output.
    Wrap the response with ```.
    
    For example:
    ```
    id, item, classified_type
    ````
    
    Input CSV file:
    %s
    """ % items

    print(prompt)
    logging.info(prompt)
    # Generate a response from the DeepSeek-R1 model
    response = ollama.generate(model="deepseek-r1:14b", prompt=prompt)

    # Output the response
    print("=================================")
    print(response["response"])
    logging.info(response["response"])


    extracted_text = re.search(r'<think>.*?</think>.*?```(.*?)```', response["response"], re.DOTALL).group(1).strip()

    return extracted_text


def get_analysis(productive_apps, unproductive_apps):
    prompt = """
    You are my personal assistant. Based on my application/website usage statistics, generate a report with insights and analysis of my focus.  
    Each value are time spent on app/website. Add Total time spent across all categories. Do not use tables.
    Wrap the response with ```. Response should be in Markdown format. Outlining the total productive time, 
    followed by each application's contribution, then list out the unproductive activities. Craft a report that's both 
    informative and easy to digest, providing clear insights into the user's application usage patterns. 
    Do not include items with up to 60 sec time spent. 
    
    productive apps = %s
    unproductive = %s
    """ % (productive_apps, unproductive_apps)

    print(prompt)
    logging.info(prompt)
    # Generate a response from the DeepSeek-R1 model
    response = ollama.generate(model="deepseek-r1:14b", prompt=prompt)

    # Output the response
    print("=================================")
    print(response["response"])
    logging.info(response["response"])

    extracted_text = re.search(r'<think>.*?</think>.*?```(.*?)```', response["response"], re.DOTALL).group(1).strip()

    if extracted_text.startswith("markdown"):
        extracted_text = extracted_text[8:]
    return extracted_text