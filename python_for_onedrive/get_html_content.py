def get_html_content(salutation_and_name, email_body):
  return f"""
    <!DOCTYPE html>
    <html>
    <head>
      <style>
        body {{
          font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
          background-color: #f5f7fa;
          margin: 0;
          padding: 0;
        }}

        .email-wrapper {{
          max-width: 600px;
          margin: auto;
          background-color: #ffffff;
          border-radius: 6px;
          overflow: hidden;
          box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}

        .header {{
          background-color: #004578;
          color: white;
          padding: 20px 30px;
          text-align: center;
        }}

        .header h1 {{
          margin: 0;
          font-size: 22px;
        }}

        .content {{
          padding: 30px;
          color: #333333;
          font-size: 16px;
          line-height: 1.6;
        }}

        .button {{
          display: inline-block;
          margin-top: 20px;
          padding: 12px 24px;
          background-color: #0078d4;
          color: #ffffff;
          text-decoration: none;
          border-radius: 4px;
          font-weight: bold;
        }}

        .footer {{
          padding: 20px 30px;
          background-color: #f0f0f0;
          font-size: 12px;
          color: #777777;
          text-align: center;
        }}
      </style>
    </head>
    <body>
      <div class="email-wrapper">
        <div class="header">
          <h1>Corporate Quarterly Update</h1>
        </div>

        <div class="content">
          <p>{salutation_and_name}</p>

          <p>{email_body}</p>

          <p>
            We are pleased to share the highlights from Q1 2025.
            Thanks to your hard work and dedication, we've
            exceeded our performance targets across multiple
            departments.
          </p>

          <p>
            To view the full report and key takeaways,
            please click the button below:
          </p>

          <a
            href="https://1drv.ms/x/c/66af906d87eb4a94/EY9dnA9TDqRLqxJFLBejqVwBDzx6pAc7WBQHKlUv4jJWpA?e=nmgNGJ"
            class="button"
            style="
              color: #ffffff;
              background-color: #0078d4;
              text-decoration: none;
              padding: 12px 24px;
              border-radius: 4px;
              display: inline-block;
              font-weight: bold;
            "
          >
            View Full Report
          </a>

          <p>Thank you for your continued commitment to excellence.</p>

          <p>Best regards,<br>Corporate Communications</p>
        </div>

        <div class="footer">
          This message is intended for internal use only.
          If you received this in error, please contact
          IT support.
        </div>
      </div>
    </body>
    </html>
  """