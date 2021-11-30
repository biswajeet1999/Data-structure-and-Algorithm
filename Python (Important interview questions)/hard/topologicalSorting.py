
class JobNode:
   def __init__(self, job):
      self.job = job
      self.prereq = []
      self.isProcessing = False
      self.isProcessed = False


class JobGraph:
   def __init__(self, jobs, deps):
      self.jobs = []
      self.graph = {}
      self.addJobs(jobs)
      self.addDependencies(deps)
   
   def addNode(self, job):
      self.graph[job] = JobNode(job)
      self.jobs.append(self.graph[job])

   def addJobs(self, jobs):
      for job in jobs:
         self.addNode(job)

   def getNode(self, job):
      if job  not in self.graph:
         self.graph[job] = JobNode(job)
      return self.graph[job]

   def addDependency(self, job, prereq):
      jobNode = self.getNode(job)
      prereqNode = self.getNode(prereq)
      jobNode.prereq.append(prereqNode)

   def addDependencies(self, deps):
      for prereq, job in deps:
         self.addDependency(job, prereq)

def topologicalSortHelper(jobGraph, job, orderedJobs):
   if job.isProcessed == True:
      return True
   if job.isProcessing == True:
      return False
   prereqs = job.prereq
   job.isProcessing = True
   for prereq in prereqs:
      status = topologicalSortHelper(jobGraph, prereq, orderedJobs)
      if status == False:
         return False
   job.isProcessing = False
   job.isProcessed = True
   orderedJobs.append(job.job)
   return True

# O(E+V) time | O(E) space (worst case E no of call stack in case of linear graph and another E for orderedJobs list)
def topologicalSort(jobs, deps):
   jobGraph = JobGraph(jobs, prereq)
   orderedJobs = []
   for job in jobGraph.jobs:
      if not job.isProcessed:
         status = topologicalSortHelper(jobGraph, job, orderedJobs)
         if status == False:
            print("cycle detected.")
            return
   return orderedJobs


jobs = [1, 2, 3, 4]
prereq = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
print(topologicalSort(jobs, prereq))