#!/usr/bin/env python3
"""
clean-urls.py — Strip tracking/UTM params from a OneTab dump.
Usage:
  echo "URL | Title" | python3 clean-urls.py
  python3 clean-urls.py dump.txt
"""

import sys
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

STRIP_PARAMS = {
    # UTM
    'utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term',
    # Google Ads
    'gclid', 'gclsrc', 'gad_source', 'gad_campaignid', 'gad_creativeid',
    # Google/Apple campaign params
    'pt', 'mt', 'ct', 'campaign_id', 'is_sa',
    'android-min-version', 'ios-min-version',
    # Bing / Edge search noise
    'pglt', 'qs', 'pq', 'sk', 'sc', 'cvid', 'gs_lcrp',
    'FORM', 'PC', 'ucpdpc', 'ntref', 'filters',
    # Misc tracking
    'showOnlyQuestions', 'lnk', 'p', 'impressionid',
    # Figma UI state (node-id & t are panel state, not content)
    'node-id', 't',
    # Flywire UI
    'hideUserManagement',
}

def clean_url(url: str) -> str:
    url = url.strip()
    try:
        parsed = urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            return url
        params = parse_qs(parsed.query, keep_blank_values=True)
        clean_params = {k: v for k, v in params.items() if k not in STRIP_PARAMS}
        clean_query = urlencode(clean_params, doseq=True)
        return urlunparse((
            parsed.scheme, parsed.netloc, parsed.path,
            parsed.params, clean_query, parsed.fragment
        ))
    except Exception:
        return url

def main():
    source = sys.argv[1] if len(sys.argv) > 1 else '-'
    lines = open(source) if source != '-' else sys.stdin
    for line in lines:
        line = line.strip()
        if not line:
            print(); continue
        if ' | ' in line:
            url_part, title = line.split(' | ', 1)
            print(f"{clean_url(url_part)} | {title.strip()}")
        else:
            print(clean_url(line))

if __name__ == '__main__':
    main()
