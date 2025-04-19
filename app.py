import gradio as gr
from api import classify_email

def process_email(email_body):
    response = classify_email({"email_body": email_body})
    return (
        response["masked_email"],
        response["category_of_the_email"],
        response["list_of_masked_entities"]
    )

iface = gr.Interface(
    fn=process_email,
    inputs=gr.Textbox(lines=8, label="Paste your support email here"),
    outputs=[
        gr.Textbox(label="Masked Email"),
        gr.Textbox(label="Predicted Category"),
        gr.JSON(label="Masked Entities")
    ],
    title="Akaike Email Classifier 🚀",
    description="Paste support emails. The system will mask personal info and classify the email into predefined categories."
)

if __name__ == "__main__":
    iface.launch()
