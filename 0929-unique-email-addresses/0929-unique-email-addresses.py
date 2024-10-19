class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '')
            
            if '+' in local:
                index = local.index('+')
                local = local[:index]
        
            unique.add(local + '@' + domain)
        
        return len(unique)