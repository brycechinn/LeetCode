class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        
        for email in emails:
            at_index = email.index('@')
            local_name, domain_name = email[:at_index], email[at_index:]
            local_name = local_name.replace('.', '')
            
            if '+' in local_name:
                plus_index = local_name.index('+')
                local_name = local_name[:plus_index]
        
            unique.add(local_name + domain_name)
        
        return len(unique)