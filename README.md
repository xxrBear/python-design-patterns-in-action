# Python 设计模式实战

## 简介

在软件工程领域，设计模式是应对软件设计中经常出现的一些问题，总结出的一套通用解决方案。它们通常被视为应对特定问题的最佳实践。

合理地运用设计模式，能够有效提升系统中代码的复用性，减少重复开发工作，降低因代码冗余带来的维护负担。同时，良好的模式设计有助于明确系统各个模块的职责边界，使系统结构更加清晰，耦合度更低，从而显著增强项目整体的可维护性与可扩展性。当需求变更或功能扩展时，良好的设计模式可以帮助开发者可以在不影响现有功能的前提下，灵活地对系统进行调整。


## 设计模式的类型

| **创建型设计模式**                                   | **结构型设计模式**                          | **行为型设计模式**                                        |
| ---------------------------------------------------- | ------------------------------------------- | --------------------------------------------------------- |
| [单例模式](examples/creational/singleton)            | [代理模式](examples/structural/proxy)       | [模板方法模式](examples/behavioral/template_method)       |
| [简单工厂模式](examples/creational/sample_factory)   | [适配器模式](examples/structural/adapter)   | [策略模式](examples/behavioral/strategy)                  |
| [工厂方法模式](examples/creational/factory)          | [装饰器模式](examples/structural/decorator) | [观察者模式](examples/behavioral/observers)               |
| [抽象工厂模式](examples/creational/abstract_factory) | [组合模式](examples/structural/composite)   | [访问者模式](examples/behavioral/visitor)                 |
| [建造者模式](examples/creational/builder)            | [桥接模式](examples/structural/bridge)      | [命令模式](examples/behavioral/command)                   |
| [原型模式](examples/creational/prototype)            | [外观模式](examples/structural/facade)      | [中介者模式](examples/behavioral/mediator)                |
|                                                      | [享元模式](examples/structural/flyweight)   | [备忘录模式](examples/behavioral/memento)                 |
|                                                      |                                             | [状态模式](examples/behavioral/state)                     |
|                                                      |                                             | [迭代器模式](examples/behavioral/iterator)                |
|                                                      |                                             | [解释器模式](examples/behavioral/interpreter)             |
|                                                      |                                             | [责任链模式](examples/behavioral/chain_of_responsibility) |

## 危险区


设计模式很容易被滥用，因此在引入设计模式之前，我们应充分分析当前系统的规模、复杂度以及后期可能的变更需求。对于规模较小、业务逻辑单一的系统，过度的模式设计往往弊大于利。只有当系统确实存在可扩展性、可维护性等方面的问题时，才值得考虑引入相应的设计模式。

对此，通常最佳的做法是：优先实现最小可用产品（MVP），在核心功能完整、可用性达标的基础上，随着项目的发展，针对实际遇到的可维护性或可扩展性问题，再分阶段引入合适的设计模式对系统进行优化。切忌在尚未明确实际问题之前，预先引入过多复杂结构。

设计模式不是软件开发的银弹，要切实理解每个模式背后的动机与适用场景，避免为了追求所谓 "设计美学" 而盲目增加不必要的设计模式，导致维护变得困难。

总结：

> 合理的使用设计模式，避免增加不必要的复杂度

## 测试

**运行所有测试**
```shell
python -m unittest discover tests
```
