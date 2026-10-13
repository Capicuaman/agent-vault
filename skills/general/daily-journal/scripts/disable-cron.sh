#!/usr/bin/env bash
# Disable the journal automation cron job (removes the line, preserves all other cron jobs)

# Check if enabled
if ! crontab -l 2>/dev/null | grep -q "journal_agent.py"; then
    echo "⏸️  Journal agent cron is already DISABLED (not found in crontab)"
    exit 0
fi

# Remove the journal_agent line, keep everything else
crontab -l 2>/dev/null | grep -v "journal_agent.py" | crontab -

echo "⏸️  Journal agent cron DISABLED"
echo ""
echo "Your other cron jobs are untouched."
echo "To re-enable: run enable-cron.sh"
echo "To run manually: /usr/bin/python3 .../journal_agent.py --force --live"
