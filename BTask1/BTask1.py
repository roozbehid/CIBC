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

    def findDependency(self, depList, installed):
        for dep in depList:
            if dep not in installed:
                dep.findDependency(dep.dependencies, installed)
            
        installed.append(self)

    def findEnvDependency(self):
        if self.env == None:
            self.findDependency(self.dependencies,self.installed)
        else:
            self.findDependency(self.env.dependencies,self.installed)
        
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




