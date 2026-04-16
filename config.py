"""
Configuration defaults for Discord Guardian Bot.
These values are used when a guild hasn't customized its settings.
"""

# ─── Anti-Nuke Thresholds ────────────────────────────────────────────
# Maximum actions allowed within the time window before triggering protection

ANTINUKE_DEFAULTS = {
    # Channel protection
    "max_channel_delete": 3,        # Max channels deleted within window
    "max_channel_create": 5,        # Max channels created within window

    # Role protection
    "max_role_delete": 3,           # Max roles deleted within window
    "max_role_create": 5,           # Max roles created within window

    # Ban/Kick protection
    "max_bans": 5,                  # Max bans within window
    "max_kicks": 5,                 # Max kicks within window

    # Webhook protection
    "max_webhook_create": 3,        # Max webhooks created within window

    # Emoji protection
    "max_emoji_delete": 5,          # Max emojis deleted within window

    # Time window in seconds for all thresholds above
    "action_window": 10,

    # Punishment: "strip_roles", "ban", "kick"
    "punishment": "strip_roles",

    # Whether anti-nuke is enabled by default
    "enabled": True,
}

# ─── Anti-Raid Thresholds ────────────────────────────────────────────

ANTIRAID_DEFAULTS = {
    # Mass join detection
    "max_joins": 10,                # Max joins within join_window
    "join_window": 8,               # Seconds to track joins

    # Minimum account age (in days) to auto-kick new accounts
    "min_account_age": 7,

    # Message spam detection
    "max_messages": 7,              # Max messages per user within msg_window
    "msg_window": 5,                # Seconds

    # Mention spam detection
    "max_mentions": 5,              # Max mentions per message
    "max_mention_msgs": 3,          # Max messages with mentions within window

    # Link spam detection
    "max_links": 3,                 # Max links per user within msg_window

    # Duplicate message detection
    "max_duplicates": 3,            # Max identical messages within window

    # Auto-lockdown on raid detection
    "auto_lockdown": True,
    "lockdown_duration": 300,       # Seconds (5 minutes)

    # Punishment: "kick", "ban", "mute", "timeout"
    "spam_punishment": "timeout",
    "raid_punishment": "kick",

    # Timeout duration in seconds (for timeout punishment)
    "timeout_duration": 600,        # 10 minutes

    # Whether anti-raid is enabled by default
    "enabled": True,
}

# ─── Logging ─────────────────────────────────────────────────────────

LOGGING_DEFAULTS = {
    "log_channel_name": "guardian-logs",
    "log_antinuke": True,
    "log_antiraid": True,
    "log_moderation": True,
}

# ─── Bot Settings ────────────────────────────────────────────────────

BOT_PREFIX = "!"
BOT_STATUS = "Guarding your server 🛡️"
EMBED_COLOR = 0x2B2D31       # Dark embed color
SUCCESS_COLOR = 0x57F287     # Green
WARNING_COLOR = 0xFEE75C     # Yellow
DANGER_COLOR = 0xED4245      # Red
INFO_COLOR = 0x5865F2        # Blurple

# Database path
DATABASE_PATH = "guardian.db"
