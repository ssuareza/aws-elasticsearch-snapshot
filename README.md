
A cheat sheet on how to take and Elasticsearch Snapshot.

## References
Oficial documentation: https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains-snapshots.html

Steps in video: https://www.youtube.com/watch?v=FmLmyvH83Ng

## Registering a Manual Snapshot Repository

This one-time operation requires that you sign your AWS request with credentials that are allowed to access.

1.- Add your values in "register-repo.py" script (section "# Your values here").

2.- Install dependencies:
```sh
pip install boto3 --user
pip install requests-aws4auth --user
``` 

3.- Run script:
```sh
python register-repo.py
```

Output should be:
```
200
{"acknowledged":true}
```