# ez-SYN-TCP-FLOOD
The simplest TCP SYN Flooder 


Read more on SYN Flooding: https://en.wikipedia.org/wiki/SYN_flood 


#### Catch the flooding with something as simple as this in your Intrusion Detection System
```
alert tcp any any -> $HOME_NET any (flags: S; msg:"Possible TCP SYN Flood"; flow: stateless; threshold: type both, track by_src, count 50, seconds 10; sid:10001;rev:1;)
```




### Catch the flooding in an IPS setting 

Rules (rules/local.rules) 

```
alert icmp any any -> any any (msg: "IP packet detected"; sid: 101; rev: 1;) 

alert tcp any any -> any any (flags: S; msg: "Possible TCP SYN Flood"; flow: stateless; threshold: type both, track by_src, count 2, seconds1; sid:100; rev:1;) 
```

Pre Proc Rules (preproc_rules/decoder.rules) 
```
rate_filter gen_id 1, sig_id 101, track by_rule, count 3, seconds 5, new_action drop, timeout 10 

rate filter gen_id 1, sig_id 100, track by_rule, count 3, seconds 5, new_action drop, timeout 10 
```
