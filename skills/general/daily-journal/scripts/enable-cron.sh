#!/usr/bin/env bash
# Enable the journal automation cron job

CRON_LINE="0 10,12,14,16,18,20 * * * /usr/bin/python3 /home/capicuaman/Documents/textDump/03_RESOURCES/Workflow_Automation/journal_automation/journal_agent.py --force --live >> /home/capicuaman/Documents/textDump/03_RESOURCES/Workflow_Automation/journal_automation/cron.log 2>&1"

# Check if already enabled
if crontab -l 2>/dev/null | grep -q "journal_agent.py"; then
    echo "✅ Journal agent cron is already ENABLED"
    echo ""
    echo "Schedule: runs at 10am, 12pm, 2pm, 4pm, 6pm, 8pm daily"
    exit 0
fi

# Add the cron line
(crontab -l 2>/dev/null; echo "$CRON_LINE") | crontab -

echo "✅ Journal agent cron ENABLED"
echo ""
echo "Schedule: runs at 10am, 12pm, 2pm, 4pm, 6pm, 8pm daily"
echo "Log: /home/capicuaman/Documents/textDump/03_RESOURCES/Workflow_Automation/journal_automation/cron.log"
