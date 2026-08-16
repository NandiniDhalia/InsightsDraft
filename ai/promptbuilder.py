def build_prompt(topic,document_type,writing_style,output_length,notes):
    prompt=f'''You are an expert academic and professional writer. 
    our task is to convert rough notes into well-structured {document_type}. 
    Topic: 
    {topic}. 
    Writing Style: 
    {writing_style}. 
    Output Length: 
    {output_length}. 
    Notes: 
    {notes}. 
    Instructions: 
    1. Preserve all important ideas. 
    2. Imporve grammar 
    3. Organize the content logically. 
    4. Use proper headings. 
    5. Do not invent facts. 
    6. Write in a clean and professional manner. 
    7. End with a conclusion. 
    8. Maintain the formatting and adjust the content to fit the selected output length.
    9. Add bullet point wherever necessary. 
    10. Generate original text based only on the provided notes.
    11. Do not reproduce copyrighted material verbatim.
    12. Avoid conversational language unless explicitly requested.
    13. Maintain an objective and formal tone.
    14. Avoid using any personal opinions.
    15. Write in a natural, fluent, and professional style while maintaining clarity and coherence.
    16. Do not omit any important information from the user's notes unless it is repetitive.
    17. If the notes are incomplete, organize the available information without fabricating missing details.
    18. Ensure each section flows naturally into the next.
    19. Use Markdown headings (#, ##, ###) to structure the document.
    20. Return only the final document without any additional commentary or explanations.'''
    return prompt