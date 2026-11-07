# Bash Log Analysis

A small Bash exercise that extracts ERROR entries from a log
and writes a report containing the matching lines and error count.

## Files

| File | Purpose |
|---|---|
| [analyse-log.sh](analyse-log.sh) | Validates the input and generates the report |
| [lab.log](lab.log) | Sample log containing INFO, WARNING and ERROR entries |
| [error-report.txt](error-report.txt) | Example report |

## Run

From this directory:

```bash
bash analyse-log.sh lab.log
```

## Expected Result

For the supplied sample log, the report contains three ERROR
entries and a total error count of 3.

## What I Learned

- Validating command-line arguments and checking file existence
- Filtering log entries with grep
- Combining commands with pipes and output redirection

## Limitations

The script matches the text ERROR and overwrites error-report.txt
each time it runs. It is a learning exercise, not a production
log-monitoring tool.
