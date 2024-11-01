import random

summary_object = ["Medical Article", "Short Story", "Email", "Social Media Post",
                  "Financial Document", "Random Article", "Legal Document", "Any Peer Reviewed Journal",
                  "Song", "Poetry", "News Story", "Science Fiction", "Mythology", "Fable",
                  "Instructional Text", "Biography/Autobiography", "Debate", "Dialogue/Discussion",
                  "Product Review", "Solicitation", "Compare/Contrast", "Pros/Cons", "Psychology Article",
                  "Job Posting"]
summary_style = ["Complete Sentences", "Paragraph", "Advanced language",
                 "For children/students", "Casual/cool", "Gen Z", "numbered list", "bullet points", "concise",
                 "comedic and lighthearted", "Tell a friend", "Normal Condensation", "100 words", "3 sentences",
                 "10-12 sentences", "300 words", "none/default/natural"]
summary_format = ["With a Title", "Separate Headings", "bold words", "italic words", "containing specific terms",
                  "simple sentences", "complex sentences", "none"]

def b_summary():
    obj1 = random.choice(summary_object)
    obj2 = random.choice(summary_style)
    obj3 = random.choice(summary_format)
    obj4 = random.choice(summary_format)
    result = print(f"{obj1}\n{obj2}\n{obj3}\n{obj4}")
    return result

b_summary()



