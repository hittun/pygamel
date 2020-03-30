#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
perfab:
    Prefab资产类型，允许您存储带有组件和属性的GameObject对象。
    预制件充当模板，您可以从中创建场景中的新对象实例。
    对预制资产所做的任何编辑都会立即反映在由此产生的所有实例中，但是您也可以分别覆盖每个实例的组件和设置
# @File : perfab.py
# @Time : 2020/3/28 12:20 
# @GitHub: https://github.com/hittun/pygamel
"""
from functools import lru_cache as _lru_cache
from typing import List as _List
from typing import Type as _Type
from typing import TypeVar as _TypeVar
from typing import Any as _Any
from typing import Tuple as _Tuple

from ecs import Processor
from ecs import Transform
from ecs import GameObject

C = _TypeVar('C')
P = _TypeVar('P')


class Perfab(GameObject):

    def __init__(self, *args, **kwargs):
        self._processors = []
        self._components = {}
        self.load_prefab()
        self.reset_prefab(*args, **kwargs)

    def load_prefab(self):
        """The load_prefab method will be called when you create a Perfab instance
        """
        self.add_component(Transform())

    def reset_prefab(self, *args, **kwargs):
        for ins in args:
            self.add_component(ins)

    def clear_cache(self) -> None:
        self.get_component.cache_clear()
        self.get_components.cache_clear()
        self.get_all_components.cache_clear()

    def has_component(self, component_types: _Any) -> bool:
        """Check if Perfab has a Component of a certain type

        :param component_types:The type of Component to check for.
        :return:True if the Perfab has a Component of this type,
                 otherwise False
        """
        return component_types in self._components

    def has_components(self, *component_types: _Any) -> bool:
        """Check if Perfab has all of the specified Component types.

        :param component_types: Two or more Component types to check for.
        :return: True if the Perfab has all of the Components,
                 otherwise False
        """
        return all(comp_type in self._components for comp_type in component_types)

    def add_component(self, component_instance: _Any) -> None:
        """Add a new Component instance to Perfab.

        Add a Component instance to Perfab. If a Component of the same type
        is already assigned to the Perfab, it will be replaced.

        :param component_instance: A Component instance.
        """
        component_type = type(component_instance)
        self._components[component_type] = component_instance

        self.clear_cache()

    def remove_component(self, component_type: _Any) -> None:
        """Remove a Component instance from Perfab, by type.

        Raises a KeyError if Component type does
        not exist in the database.
        :param component_type: The type of the Component to remove.
        """
        del self._components[component_type]

        self.clear_cache()

    def _get_component(self, component_type: _Type[C]) -> C:
        """Get Component instance.

        :param component_type: The Component type to retrieve.
        :return: An Component instance.
        """
        return self._components.get(component_type, None)

    def _get_components(self, *component_types):
        """Get an Component instance sets.

        :param component_types: Two or more Component types.
        :return: An iterator for [Component1, Component2, etc] list.
        """
        comp_db = self._components
        return [comp_db[ct] for ct in component_types]

    @_lru_cache()
    def get_component(self, component_type: _Type[C]) -> _List[_Tuple[int, C]]:
        return [query for query in self._get_component(component_type)]

    @_lru_cache()
    def get_components(self, *component_types: _Type):
        return [query for query in self._get_components(*component_types)]

    @_lru_cache()
    def get_all_components(self):
        component_types = self._components.keys()
        return self.get_components(*component_types)

    def add_processor(self, processor_instance: Processor, priority=None) -> None:
        """Add a Processor instance to the World.

        :param processor_instance: An instance of a Processor,
               subclassed from the Processor class
        :param priority: A higher number is processed first.
        """
        assert issubclass(processor_instance.__class__, Processor)
        processor_instance.priority = priority
        self._processors.append(processor_instance)

    def remove_processor(self, processor_type: Processor) -> None:
        """Remove a Processor from the World, by type.

        :param processor_type: The class type of the Processor to remove.
        """
        for processor in self._processors:
            if type(processor) == processor_type:
                processor.world = None
                self._processors.remove(processor)

    def get_all_processors(self):
        return self._processors


class PrefabRender(Perfab):
    def __init__(self):
        super().__init__()


class PrefabLogic(Perfab):
    def __init__(self):
        super().__init__()
