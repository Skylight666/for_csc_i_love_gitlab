alph = {}

with open('w_aplphabet.txt', 'r') as f:
    for l in f:
        a = l.split('   ')
        alph[a[0].strip()] = float(a[1].strip())

ans = 0
s = 'TKTLSNVRKKCFDATININPQSGQVAWWSDTAVHSMFWKGLYCRTLLHKEVNNHAVIMKTWVHMRKMEFDRIYEDNIPYCELIDWVHWYDCFCWEGEYWGTANVQTVQYSRSPYIILCFQEEMTCFAHASRRLNGIKKIQWHTQRQQGMTWIWSIPGDFTEIMQHIHCMNWHSRFNANKLPALTIGEMLYIRRFHLGKEGLLACDQQLYEKIMSAHRPRARPSHTHSMFYVHWGLLYSYINGQLKDEDQTIEARKGWHGIQINNYSFNCRTDAPHDMYLSEYETFVQLRATHFTVVKCDGHKIFVWRDVHMFAPKEYKDKDWFKKCTWNMVAMWCFPLFRFPNFTQMLARIAYGCCAYSTCFRFTDLDDFNTLGAVRSRQSKGPLVYSFAWTGREFTSPPEVQSKLQKDQWLKMRQWPHGAPAGPVYFQGAHVLCQACIFRTIATLCCELHCIWSKLAGRLCQWPPNHWDIRSSFQRQTHGMYMWWDACAVRWDMNMGHVHHRMNSTFDPSWQLDRVEASMKNYCLFHYCFKAGWIAMDSPRHLMCWVKNWGWNCAFLERFPMCWWPMREGFVPGCIVKCSSMSDLWEYPKMAHPWTHISKLTPLLQEFSNNDCKANYTLVRKCINNVKEGASINSLEQKPHMKVFWSPREDMQIYATGQQHRWFSLNVRAAHSIYIEDQICNVCGSNMQILCQRFGGDGWMRGQFMYTHTRQTFMGGGHHYCKSLYLEIERWFNVSWYPTTTMFCCRACFCNMPLRCHQLFSILWTERLDATGWDCPLQHNHESHSRSHDVSRVFWWRIFGKHEVIPKSVKR'
for i in s:
    ans += alph[i]
print(ans)
