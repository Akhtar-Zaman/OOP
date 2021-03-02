import re 
class commits:
    def __init__(self):
        self.commits = []
        self.position = 1
        self.id = 0
        

    def list_of_commits(self):
        if len(self.commits)==0:
            print('No Commit yet')
        else:
            new_lst = self.commits[::-1]
            print('------List of all Commits are---------')
            for i in new_lst:
                for k, l in i.items():
                    print(k, str(l))

    def add_commit(self, tex):
        self.id = self.id+1
        self.commits = self.commits +[{self.id:tex}]
        self.position = int(len(self.commits)-1)
        

    def show_commit(self):
        uu = self.pposition()
        if len(self.commits)==0:
            print('No Commit yet')
        else:
            print(self.commits[uu][self.id])

    def Next_commit(self):
        next = self.position
        nn=''
        if next+2<=len(self.commits):
            nn = self.commits[next+1]
            self.position = self.position +1
        else:
            print("there are no more NEXT commit")
        return nn

    def prev_commit(self):
        prev = self.position
        pp =""
        if prev-1>=0:
            pp = self.commits[prev-1]
            self.position = self.position -1
        else:
            print("there are no more Previous commit")

        return pp

    def jump(self,x):   
        self.position=x-1  
        return self.commits[self.position]

    def pull(self,x):  
        self.position=x-1 
        zz = self.commits[self.position]
        del self.commits[self.position]
        self.commits.insert(0, zz)
        self.position=0


    def remove(self, x):
        del self.commits[x]

    def update(self, tex):
        self.commits[self.position] = list(tex)

    def pposition(self):
        return self.position

    

def main():
    a = commits()
    done = False
    while True:
        print('Please Enter "git init" to execute your program')
        git_init = input('')

        if git_init=='git init':
            while done==False:

                choice = input('Enter choice: ')
                c = choice.split()
                tex = re.findall(r'\"(.+?)\"', choice)
                print('')

                if c[0]=='git' and c[1]=='commit':
                    #a = commits(['akhtar', 'zaman', 'khan'])
                    a.add_commit(tex)
                elif c[0]=="git" and c[1]=="show" and c[2]=="commit":
                    a.show_commit()
                elif c[0]=="git" and c[1]=="show" and c[2]=="all" and c[3]=="commit":
                    a.list_of_commits()
                elif c[0]=='git' and c[1]== 'delete':
                    x = int(c[2])
                    a.remove(x-1)

                elif c[0]=='git' and c[1]== 'next':
                    a.Next_commit()
                    #x=x+1
                elif c[0]=='git' and c[1]== 'prev':
                    a.prev_commit()
                    # x=x-1

                elif c[0]=='git' and c[1]== 'jump':
                    x = int(c[2])
                    a.jump(x)

                elif c[0]=='git' and c[1]=='update':
                    a.update(tex)

                elif c[0]=='git' and c[1]== 'pull':
                    x = int(c[2])
                    a.pull(x)

                elif choice== 'back':
                    break
                elif choice== 'exit':
                    exit()
        elif git_init== "True":
            print('')

    

main()

