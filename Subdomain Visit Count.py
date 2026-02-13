class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count=defaultdict(int)

        for domain in cpdomains:
            new_domain=domain.split(" ")

            count=int(new_domain[0])
            full_domain=(new_domain[1])

            domain_split=full_domain.split(".")

            for i in range(len(domain_split)):
                subdomain=".".join(domain_split[i:])
                domain_count[subdomain]+=count
        return [f"{freq} {domain}" for domain, freq in domain_count.items()]
        
