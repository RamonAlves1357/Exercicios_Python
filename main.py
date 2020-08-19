#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Questions as Question

ID_questao = input(" Digite o número da questão(ex.: 1, 2, 3...): ")
ID_questao = "Question.questao" + ID_questao + "()"
print()
exec(ID_questao)