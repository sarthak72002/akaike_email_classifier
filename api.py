from models import load_model, predict_category
from utils import mask_text

# Load the pipeline once when API starts
pipeline = load_model()  # <-- FIXED HERE

def classify_email(request_dict):
    """
    Classify the email after masking PII.
    
    Args:
        request_dict (dict): {'email_body': 'email text'}
    
    Returns:
        dict: structured output including masked email, entities, and predicted category
    """
    input_email = request_dict["email_body"]  # Correct key
    masked_email, entities = mask_text(input_email)  # Mask PII
    category = predict_category(pipeline, masked_email)  # <-- USE pipeline now

    return {
        "input_email_body": input_email,
        "list_of_masked_entities": entities,
        "masked_email": masked_email,
        "category_of_the_email": category
    }

