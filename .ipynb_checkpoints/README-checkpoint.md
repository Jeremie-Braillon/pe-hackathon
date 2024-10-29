# Hackathon, mardi 29 octobre à partir de 13h45

Ce hackathon est la réalisation d'un code en groupe en utilisant des notions de l'UE12 PE: `Python`, `numpy`, `pandas`, `matplotlib`, ou autre librairie de visualisation et `git`. 

Les groupes sont là:
https://docs.google.com/spreadsheets/d/1iZIjBzyHhLI3gR73c9gYxFCaZv7ui_MzCa7XRw93r6o/edit?gid=1307595571#gid=1307595571

## à votre arrivée, vous créez un repo `github`

1. Créez un repo public `github` de nom `pe-hackathon` dans l'espace `github` d'un des élèves, en acceptant la création du fichier `readme.md` (pour que `git` fasse un premier `commit`)
2. Tous les élèves du groupe `clonent` ce repo sur leur portable
3. Le propriétaire du repo invite sur `github` les autres élèves à être `collaborator` de ce repo
4. Vous indiquez dans le spreadsheet des groupes l'`URL` de votre repo

## notebooks textuels

**Évitez surtout le format `.ipynb`** car vous allez avoir plein de conflits au moment de `merge` vos commits.

Il est possible d'écrire des notebooks Jupyter sous le format `.py`. C'est ce
qu'on vous recommande d'utiliser;  
et pour en créer un dans Jupyter vous faites
*File* -> *New Text Notebook* -> *New Python Text Notebook with Percent Format*.

(évitez aussi les `.md`, en fait vous écrivez du Python quand même principalement)

## ensuite, vous décidez de comment vous allez collaborer avec `git`

À vous de choisir entre la **manière simpliste** (où chaque élève travaille dans
son `notebook` personnel) et des **manières plus évoluées** (où tous les élèves
travaillent indifféremment tous sur tous les fichiers et résolvent les éventuels
conflits; ou alors où les élèves travaillent chacun dans leur branche, et les
mergent un jour).

**Si vous êtes débutants avec `git`**, nous vous proposons de suivre **la
méthode d'organisation basique** décrite ci-dessous;  
**si vous savez déjà vous organiser avec `git`** passez aux [**choix des sujets
(cliquez ici)**](./sujets.md)

## méthode d'organisation basique de vos repo

Dans un projet idéal, les fonctionnalités communes à tous (par exemple les
fonctions qui chargent, nettoient et préparent les données) sont mises dans un
module `python` commun (par exemple `common.py`) que vous importez dans vos
codes.

Exemple:

```python
# ce code, mis dans un notebook, n'est pas réutilisable:
df = pd.read_csv("data.csv")
df = df.rename(columns={"foo": "bar"})
```

```python
# on fait de ce code une fonction du fichier common.py
def load_data(filename):
    df = pd.read_csv(filename)
    df = df.rename(columns={"foo": "bar"})
    return df
```

```python
# et on l'utilise dans les notebooks, en important le module
import common
df = common.load_data("data.csv")
```

***Attention au problème de l'autoreload: lisez l'ANNEXE 1***

Mais, avoir dans un projet un module python commun que tout le monde importe et
modifie, augmente les chances d'avoir des conflits `git` (parfois difficiles à
résoudre quand on débute avec `git`).

Nous vous proposons une manière intermédiaire qui consiste à avoir par élève:

- un module (un simple fichier) python personnel `common_truc_.py` (si vous vous
  appelez `truc`) où vous mettez toutes vos fonctions
- un notebook personnel `notebook-truc.py` qui importe votre module python et qui en
  utilise les fonctions
- tous deux seront mis sous `git` dans votre repo
- une seule personne pouvant modifier ces fichiers, il n'y aura pas de conflits

Supposons maintenant que vous avez terminé une fonction utile à tout le groupe:

* vous le leur dites, ils importent votre module et ils utilisent votre fonction
* comme cela, petit à petit, vous allez mettre des choses en commun sans gérer
  de conflits
* pour faire évoluer votre projet, vous pourrez remettre à plat et réorganiser
  les modules python

De cette manière

- chacun travaille sur sa partie, commit régulièrement, et publie ses commits
  sur `github` (avec `git push` ), en ayant fait juste avant un `git pull` pour
  être à jour avec le repo distant

- l'intégration du projet se fait au fil de l'eau, puisque à chaque `pull` on
  fait en réalité un `merge` qui intègre les modifications des autres *(vous
  travaillez tous sur la même branche `main`)*  
**notez** que lorsque `git` fait le merge d’intégration des modifications des
autres, vous devrez donner un message (vscode s'ouvre)

- *notons qu'une autre manière de travailler est de travailler sur des branches
  différentes, l'intégration du projet se fera alors de manière explicite en
  demandant de `merge` les branches.*

## répartition des rôles

Le groupe se répartit la réalisation des analyses. Il est important, surtout en
temps limité, que chacun puisse commencer à travailler sur son module **sans
attendre que les autres** aient terminé les leurs. Faites des points
d'avancement réguliers et rapides pour contrôler que tout se passe bien:

## ANNEXE 1 Attention à l'autoreload

Lorsque vous importez un module dans un notebook, il y a **un piège à éviter**:

- en effet `Python` va charger le module **mais seulement la
  première fois**
- **et c'est voulu**, car le chargement d'un module peut être coûteux, et on ne veut pas
  le refaire à chaque fois

Ainsi:

- si vous êtes dans le notebook principal
- vous importez le module `common`
- puis ensuite vous modifiez le module `common.py` (par exemple vous avez une
  nouvelle version de la fonction `load_data`)
- et là vous réexécutez l'import de `common`

... eh bien dans ce cas-là `Python` **ne rechargera pas** le module, et vous
aurez l'impression que vos modifications ne sont **pas prises en compte**&nbsp;
!

Pour éviter ce problème, on vous a fait faire au début de l'année (le jour des
installations) une configuration de `IPython` qui permet de recharger les
modules à chaque fois;  
une fois cette configuration effectuée, tant que vous êtes dans `IPython` ou
dans un notebook, vous ne vous préoccupez plus de ce problème, tout se met à
fonctionner comme attendu.

Mais si vous avez l'impression que vos modifications ne sont pas prises en compte,
pour vérifier que cette configuration est bien faite, vous exécutez dans le terminal:

```bash
cat  ~/.ipython/profile_default/ipython_config.py
```

et vous devez voir quelque chose comme:

```python
   c.InteractiveShellApp.exec_lines = []
   c.InteractiveShellApp.exec_lines.append('%load_ext autoreload')
   c.InteractiveShellApp.exec_lines.append('%autoreload 2')
```

Si ce n'est pas le cas, reportez vous aux
[notes d'installation pour le faire](https://ue12-p24-intro.readthedocs.io/en/main/1-01-installations-nb.html#configuration-de-l-autoreload)

## ANNEXE 2 Scénario `github` de débutant

Dans un `bash`:

```bash
$ git clone git@github.com:truc/pe-hackathon.git

$ cd pe-hackathon

$ ls
readme.md

$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

$ git log
* cb4d5d3 (HEAD -> main, origin/main, origin/HEAD) Initial commit

$ git remote get-url origin
git@github.com:truc/pe-hackathon.git

$ jupyter lab &
```

Dans `jupyter lab` vous créez (remplacez `machin` par le nom de l'élève):

- un fichier `notebook_machin.py`  
  "File" -> "New Text Notebook" -> "New Python Text Notebook with Percent Format*  
- un fichier `common_machin.py`  
  "File" -> "New" -> "Python file"

Que vous mettez sous gestion de version `git`:

```bash
$ ls
common_machin.py  notebook_machin.py  README.md

$ git add notebook_machin.py common_machin.py

$ git commit -m"les fichiers de machin"
[main 52b07fb] les fichiers de machin
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 common_machin.py
 create mode 100644 notebook_machin.py

$ git l
* 52b07fb (HEAD -> main) les fichiers de machin
* cb4d5d3 (origin/main, origin/HEAD) Initial commit

$ git push
To github.com:truc/pe-hackathon.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'github.com:truc/pe-hackathon.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

**Que se passe-t-il ?**

- et bien un autre élève de votre groupe a poussé un `commit` sur le repo distant depuis le moment où vous l'avez cloné
- votre repo local n'est plus à jour vis à vis de son repo distant (son remote)
- vous devez mettre votre repo local à jour avec un `git pull`
- celui-ci *descend* localement le commit que vous n'aviez pas (`fetch`)
- puis il crée un commit qui **merge** votre commit local et celui qu'il vient de descendre
- il ouvre `vscode` pour que vous écriviez le message du nouveau `commit`
- et maintenant vous pouvez refaire votre `git push`
- vous n'avez pas de conflits à résoudre si n'avez pas modifié les mêmes endroits de fichiers

```bash
$ git pull   (qui ouvre vscode)
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 287 bytes | 287.00 KiB/s, done.
From github.com:truc/pe-hackathon
   cb4d5d3..25ba86a  main       -> origin/main
Merge made by the 'ort' strategy.
 common_bidule.py   | 0
 notebook_bidule.py | 0
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 common_bidule.py
 create mode 100644 notebook_bidule.py

$ git l
*   c7d3a2b (HEAD -> main) the merge is here 
|\  
| * 25ba86a (origin/main, origin/HEAD) les fichiers de bidule
* | 52b07fb les fichiers de machin
|/  
* cb4d5d3 Initial commit
```
