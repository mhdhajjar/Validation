import copy
import sys
from RootedRelation import *
from Soup import *
import sys

class Stack:
    def _init_(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.array = [0] * capacity

def isFull(stack):
    return (stack.top == (stack.capacity - 1))

def isEmpty(stack):
    return (stack.top == -1)

def push(stack, item):
    if (isFull(stack)):
        return
    stack.top += 1
    stack.array[stack.top] = item

def Pop(stack):
    if (isEmpty(stack)):
        return -sys.maxsize
    Top = stack.top
    stack.top -= 1
    return stack.array[Top]

def moveDisksBetweenTwoPoles(src, dest, s, d):
    pole1TopDisk = Pop(src)
    pole2TopDisk = Pop(dest)

    if (pole1TopDisk == -sys.maxsize):
        push(src, pole2TopDisk)
        moveDisk(d, s, pole2TopDisk)

    elif (pole2TopDisk == -sys.maxsize):
        push(dest, pole1TopDisk)
        moveDisk(s, d, pole1TopDisk)

    elif (pole1TopDisk > pole2TopDisk):
        push(src, pole1TopDisk)
        push(src, pole2TopDisk)
        moveDisk(d, s, pole2TopDisk)

    else:
        push(dest, pole2TopDisk)
        push(dest, pole1TopDisk)
        moveDisk(s, d, pole1TopDisk)

def moveDisk(fromPeg, toPeg, disk):
    print("Move the disk", disk, "from '", fromPeg, "' to '", toPeg, "'")

def Hanoi_Instance(nbStacks, nbDisks):
    i_conf = HanoiConfiguration(nbStacks, nbDisks)
    soup = SoupProgram(i_conf)
    for i in range(nbStacks):
        for j in range(nbStacks):
            soup.add(Rule(f'{i}-{j}', guard(i, j), action_def(i, j)))
    return soup


def guard(s, t):
    return lambda c: len(c[s]) and (len(c[t]) == 0 or c[s][-1] < c[t][-1])


def action_def(s, t):
    def action(c):
        disk = c[s].pop()
        c[t].append(disk)

    return action


class Hanoi(RootedRelation, PossibleActions):

    def _init_(self, nbStacks, nbDisks):
        self.nbDisks = nbDisks
        self.nbStacks = nbStacks

    def initial(self):
        return [HanoiConfiguration(self.nbStacks, self.nbDisks)]

    def roots(self):
        pass

    def next(self, n):
        next_states = []
        for i in range(self.nbStacks):
            new_node = copy.deepcopy(n)
            if new_node[i]:
                disk = new_node[i].pop()
                for j in range(self.nbStacks):
                    if i != j and (not new_node[j] or new_node[j][-1] > disk):
                        temp = copy.deepcopy(new_node)
                        temp[j].append(disk)
                        next_states.append(temp)
        return next_states

    def is_accepting(self, c):
        k = 0
        if not c[-1]:
            return False
        for disk in c[-1]:
            if disk != self.nbDisks - k:
                return False
            k = k + 1
        return True


class HanoiConfiguration(list):
    def _init_(self, nbStacks, nbDisks):
        list._init_(self, [[(nbDisks - i) for i in range(nbDisks)]] + [[] for _ in range(nbStacks - 1)])

    def _hash_(self):
        hash = 0
        maxi = max(self)[0]
        for stack in self:
            hash += sum(stack) * maxi
            maxi *= 2
        return hash

    def _eq_(self, conf):
        if len(self) != len(conf):
            return False
        for i in range(len(self)):
            if len(self[i]) != len(conf[i]):
                return False
            for j in range(len(self[i])):
                if conf[i][j] != self[i][j]:
                    return False
        return True

import copy
import sys
from RootedRelation import *
from Soup import SoupProgram
from Soup import *
import sys

class Stack:
    def _init_(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.array = [0] * capacity

def isFull(stack):
    return (stack.top == (stack.capacity - 1))

def isEmpty(stack):
    return (stack.top == -1)

def push(stack, item):
    if (isFull(stack)):
        return
    stack.top += 1
    stack.array[stack.top] = item

def Pop(stack):
    if (isEmpty(stack)):
        return -sys.maxsize
    Top = stack.top
    stack.top -= 1
    return stack.array[Top]

def moveDisksBetweenTwoPoles(src, dest, s, d):
    pole1TopDisk = Pop(src)
    pole2TopDisk = Pop(dest)

    if (pole1TopDisk == -sys.maxsize):
        push(src, pole2TopDisk)
        moveDisk(d, s, pole2TopDisk)

    elif (pole2TopDisk == -sys.maxsize):
        push(dest, pole1TopDisk)
        moveDisk(s, d, pole1TopDisk)

    elif (pole1TopDisk > pole2TopDisk):
        push(src, pole1TopDisk)
        push(src, pole2TopDisk)
        moveDisk(d, s, pole2TopDisk)

    else:
        push(dest, pole2TopDisk)
        push(dest, pole1TopDisk)
        moveDisk(s, d, pole1TopDisk)

def moveDisk(fromPeg, toPeg, disk):
    print("Move the disk", disk, "from '", fromPeg, "' to '", toPeg, "'")

def Hanoi_Instance(nbStacks, nbDisks):
    i_conf = HanoiConfiguration(nbStacks, nbDisks)
    soup = SoupProgram(i_conf)
    for i in range(nbStacks):
        for j in range(nbStacks):
            soup.add(Rule(f'{i}-{j}', guard(i, j), action_def(i, j)))
    return soup


def guard(s, t):
    return lambda c: len(c[s]) and (len(c[t]) == 0 or c[s][-1] < c[t][-1])


def action_def(s, t):
    def action(c):
        disk = c[s].pop()
        c[t].append(disk)

    return action


class Hanoi(RootedRelation, PossibleActions):

    def _init_(self, nbStacks, nbDisks):
        self.nbDisks = nbDisks
        self.nbStacks = nbStacks

    def initial(self):
        return [HanoiConfiguration(self.nbStacks, self.nbDisks)]

    def roots(self):
        pass

    def next(self, n):
        next_states = []
        for i in range(self.nbStacks):
            new_node = copy.deepcopy(n)
            if new_node[i]:
                disk = new_node[i].pop()
                for j in range(self.nbStacks):
                    if i != j and (not new_node[j] or new_node[j][-1] > disk):
                        temp = copy.deepcopy(new_node)
                        temp[j].append(disk)
                        next_states.append(temp)
        return next_states

    def is_accepting(self, c):
        k = 0
        if not c[-1]:
            return False
        for disk in c[-1]:
            if disk != self.nbDisks - k:
                return False
            k = k + 1
        return True


class HanoiConfiguration(list):
    def _init_(self, nbStacks, nbDisks):
        list._init_(self, [[(nbDisks - i) for i in range(nbDisks)]] + [[] for _ in range(nbStacks - 1)])

    def _hash_(self):
        hash = 0
        maxi = max(self)[0]
        for stack in self:
            hash += sum(stack) * maxi
            maxi *= 2
        return hash

    def _eq_(self, conf):
        if len(self) != len(conf):
            return False
        for i in range(len(self)):
            if len(self[i]) != len(conf[i]):
                return False
            for j in range(len(self[i])):
                if conf[i][j] != self[i][j]:
                    return False
        return True