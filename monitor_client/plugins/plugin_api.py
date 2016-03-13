#!/usr/bin/env python
#coding:utf-8

import load, cpu, memory


def get_load_info():
    return load.monitor()


def get_cpu_info():
    return cpu.monitor()


def get_memory_info():
    return memory.monitor()


