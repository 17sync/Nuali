# Design

This phase focuses on defining the system architecture, components, and workflows of the Twitter/X bot **Nuali**. The goal is to ensure the system is modular, secure, and compliant with Twitter/X API policies.

**System Architecture:**
Nuali follows a modular, script-based architecture where each core functionality is handled independently. This improves maintainability and scalability.

**Main Components:**
- Authentication Module
- Tweet Scheduler
- Keyword Scanner
- Interaction Handler
- Reply Generator
- Error & Rate Limit Handler
- Logging Module

**Component Design:**

- **Authentication Module:**
    - Uses Twitter/X API keys and tokens.
    - Credentials are stored securely using environment variables.
    - Authentication is handled via the Tweepy library.

- **Tweet Scheduler:**
    - Posts tweets at fixed intervals (1 hour).
    - Uses time-based scheduling (`time.sleep()` or scheduler libraries).
    - Prevents excessive posting to comply with API rules.

- **Keyword Scanner:**
    - Monitors tweets using predefined keywords.
    - Filters relevant tweets for retweeting, liking, or replying.
    - Ensures no duplicate interactions occur.

- **Interaction Handler:**
    - Performs actions such as:
        - Liking tweets
        - Retweeting tweets
        - Replying to tweets
    - Validates actions to avoid spam-like behavior.

- **Reply Generator:**
    - Generates human-like and respectful replies.
    - Replies are predefined or template-based.
    - Ensures responses are non-toxic and policy-compliant.

- **Error & Rate Limit Handler:**
    - Detects API rate limits and pauses execution accordingly.
    - Handles network failures and API errors gracefully.
    - Retries actions after cooldown periods.

- **Logging Module:**
    - Logs bot activities such as tweets posted and interactions made.
    - Helps with debugging and monitoring bot behavior.

**Data Flow:**
1. Authenticate with Twitter/X API.
2. Fetch tweets based on keywords.
3. Analyze tweet relevance.
4. Perform allowed interactions.
5. Log actions and errors.
6. Wait for the next execution cycle.

**Security Design:**
- API keys are never hardcoded.
- Environment variables or `.env` files are used.
- Sensitive data is excluded from version control.

**Design Constraints:**
- Must comply with Twitter/X automation rules.
- Limited by Non-Elevated API access.
