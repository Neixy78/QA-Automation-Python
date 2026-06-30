from playwright.sync_api import sync_playwright

def test_robust_navigation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # We will try to open a fake, broken URL to simulate a server crash
        broken_url = "https://this-website-does-not-exist-at-all-guc.com"
        
        try:
            print(f"STEP: Attempting to connect to: {broken_url}")
            # Set a strict 5-second timeout so the script doesn't hang forever
            page.goto(broken_url, timeout=5000) 
            print("SUCCESS: Loaded page successfully.")
            
        except Exception as error_message:
            # Instead of crashing your software, the script catches the error cleanly
            print("\n[QA ALERT] SYSTEM CAUGHT A CRITICAL ERROR SUCCESSFULLY!")
            print(f"[REASON]: {error_message}")
            print("[ACTION]: Sending alert log to development team... [SIMULATED]\n")
            
        finally:
            # This block ALWAYS runs, ensuring the browser closes safely to save computer memory
            print("STEP: Safely closing the browser session.")
            browser.close()

# Run the error-handling test
test_robust_navigation()
