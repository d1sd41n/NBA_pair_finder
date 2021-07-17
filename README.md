# NBA_pair_finder

to use the script that finds pairs of players, execute the python file "nba_main.py" passing it as an argument the number that you want to use as the sum of pairs.

example:

```console
$ python nba_main.py 139

-Brevin Knight  Nate Robinson
-Nate Robinson  Mike Wilks
```

You can also run it as linux executable

```console
$ ./nba_main.py 139

-Brevin Knight  Nate Robinson
-Nate Robinson  Mike Wilks
```

## Notes
For the moment the algorithm returns pairs of repeated players that have the same height

```console
$ ./nba_main.py 138

-Chucky Atkins  Nate Robinson
-Brevin Knight  Mike Wilks
-Nate Robinson  Speedy Claxton
-Mike Wilks  Brevin Knight
```
