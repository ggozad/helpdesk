from fastapi_mail import MessageSchema

from backend.app import app
from backend.utils.mail import get_mailer, EmailSchema


@app.post("/test/")
async def test(email: EmailSchema):
    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=email.dict().get(
            "email"
        ),  # List of recipients, as many as you can pass
        body="""
            <p>Hi this test mail, thanks for using Fastapi-mail</p>
        """,
        subtype="html",
    )
    mailer = get_mailer()
    await mailer.send_message(message)
    return {"result": "ok"}