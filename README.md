# chatterbot-weichat

一. 聊天机器人组成模块

提问处理->信息检索->答案抽取

1. 提问处理模块
   
   提问处理模块的三项重要工作：查询关键词生成，答案类型确定，句法和语义分析。
  - 查询关键词生成：就是从你的提问中提取关键的几个关键词。通过提问的中心词，再关联出几个扩展词，网上一搜一大批资料就来了，然后这些都是原始资料，还要继续处理。所以需要确认答案类型。
  - 答案类型确认：就是为了确定你的提问属于哪一类，如果你问的是时间、地点、和你问的技术方案，后续处理是不一样的。
  - 句法和语义分析：这个是对问题的深层含义做一个剖析。比如你的问题是 聊天机器人怎么做，那么机器人需要知道你要问的是 ‘聊天机器人的研发方法’

2. 检索模块

   检索模块跟搜索引擎比较像，就是根据查询关键词得信息检索，返回句子或者段落，这部分就是需要处理的原料。
   
3. 答案抽取模块

   答案抽取模块是计算量最大的部分，它主要通过分析和推理从检索出的句子或段落里抽取和提问一致的实体，再根据概率最大对候选答案排序，注意：这里是‘候选答案’，很难给一个完全正确的答案，很有可能给出多个结果，最后再选出一个来。

二. 聊天机器人涉及技术

  - 海量文本知识表示（网络文本资源获取，机器学习方法，大规模语义计算和推理，知识表示体系，知识库构建）
  - 问句解析（中文分词，词性标注，实体标注，概念类别标注，句法分析，语义分析，逻辑结构标注，指代消解，关联关系标注，问句分类（简单句还是复杂句，实体型还是段落型还是篇章级问题），答案类别确定） 
  - 答案生成与过滤（候选答案抽取，关系推演（并列还是递进还是因果），吻合程度判断，噪声过滤）

三. 聊天机器人的技术分类

   聊天机器人技术分为四种类似：基于检索的技术，基于模式匹配的技术，基于自然语言理解的技术，基于统计翻译模型的技术。
   优缺点：
    1）基于检索的技术就是信息检索，简单易实现，但是无法从句法关系和语义关系给出答案，也就是搞不定推理问题，所以直接pass掉。
    2）基于模式匹配的技术就是把问题往已经梳理好的几种模式上去靠，这种做推理简单，但是模式我们涵盖不全，所以也pass掉，
    3）基于自然语言理解就是把浅层分析加上句法分析，语义分析都融入进来做的补充和改进。
    4）基于统计翻译就是把问句里的疑问词留出来，然后和候选答案做配对，能对齐就是答案，对不起就失败了，所以pass掉。
