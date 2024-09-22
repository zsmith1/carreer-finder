import os
import urllib.request
import json
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    supabase = create_client(os.environ.get('SUPABASE_URL'), os.environ.get('SUPABASE_KEY'))
    companies = supabase.table('Company').select('*').execute()
    
    for company in companies.data:
        text = urllib.request.urlopen(company['careers_url']).read()
        new_html = text.decode('utf-8')
        
        last_scrape = (
            supabase.table('Scrapes')
            .select('*')
            .eq('company_id', company['id'])
            .order('created_at', desc=True)
            .limit(1)
            .execute()
        )

        insert_json = json.dumps({"html": new_html})
        response = (
            supabase.table('Scrapes')
            .insert({'value': insert_json, 'company_id': company['id']})
            .execute()
        )
        
        if not last_scrape.data:
            continue
        
        old_html = json.loads(last_scrape.data[0]['value'])['html']
        
        if old_html != new_html:
            print(f'{company["name"]} has updated their careers page!')