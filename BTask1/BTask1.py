class Project:
    def  __init__(self, projectName, env = None):
        self.projectName = projectName
        self.env = env
        self.dependencies = []
        self.installed = []

        if self.env != None:
            self.env.dependencies.append(self)

    def addDependency(self, project):
        self.dependencies.append(project)
        if self.env != None:
            if self not in self.env.dependencies:
                self.env.dependencies.append(self)

    def findDependency(self, depList, installed, traversed):
        traversed.append(self)
        for dep in depList:
            if dep not in installed:
                if dep in traversed:
                    text = "Circular dependency for %s to %s" % (self.projectName, dep.projectName)
                    print(text)
                    raise Exception(text)
                dep.findDependency(dep.dependencies, installed, traversed)
            
        installed.append(self)

    def findEnvDependency(self):
        traversed = []
        if self.env == None:
            self.findDependency(self.dependencies,self.installed, traversed)
        else:
            self.findDependency(self.env.dependencies,self.installed, traversed)
        
        for project in self.installed:
            print(project.projectName)


master = Project("master")
a = Project("a", master)
b = Project("b", master)
c = Project("c", master)
d = Project("d", master)
e = Project("e", master)
f = Project("f", master)

d.addDependency(a)
b.addDependency(f)
d.addDependency(b)
a.addDependency(f)
c.addDependency(d)

master.findEnvDependency()

# --- create circular dependency
master2 = Project("master2")
a = Project("a", master2)
b = Project("b", master2)
c = Project("c", master2)
d = Project("d", master2)

a.addDependency(b)
b.addDependency(c)
c.addDependency(d)
d.addDependency(b)

master2.findEnvDependency()


