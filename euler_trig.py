from manim import *

class EulerToTrig(Scene):
    def construct(self):
        
        #Master Identity
        euler = MathTex(r"\text{Euler's Formula: } \mathrm{e}^{i\theta}\,= \cos \theta + i \sin \theta").to_edge(UP)
        
        #Sum Identities
        sum_1 = MathTex(r"\mathrm{e}^{i(\alpha + \beta)} = \mathrm{e}^{i(\alpha)} + \mathrm{e}^{i(\beta)}").next_to(euler, DOWN)
        sum_2 = MathTex(r"\cos(\alpha + \beta) + i\sin(\alpha + \beta) = (\cos \alpha + i\sin\alpha)(\cos \beta + i\sin\beta)").next_to(sum_1, DOWN)
        sum_3 = MathTex(r"\cos(\alpha + \beta) + i\sin(\alpha + \beta) = \cos \alpha \cdot\cos \beta + \cos \alpha\cdot i\sin\beta + i\sin\alpha\cdot\cos\beta + i\sin\alpha\cdot i\sin\beta").next_to(sum_2, DOWN)
        sum_sin_ident_with_i = MathTex(r"i\sin(\alpha + \beta) = \sin(\alpha + \beta) = i \sin\alpha\cdot\cos\beta + \cos\alpha\cdot i\sin\beta").next_to(sum_3, DOWN)
        sum_sin_ident_without_i = MathTex(r"\sin(\alpha + \beta) = i \sin\alpha\cdot\cos\beta + \cos\alpha\cdot i\sin\beta").next_to(sum_sin_ident_with_i, DOWN)
        sum_cos_ident = MathTex(r"\cos(\alpha + \beta) = \cos \alpha \cdot \cos\beta - \sin \alpha \cdot \sin \beta").next_to(sum_sin_ident_without_i, DOWN)

        #Difference Identities
        diff_1 = MathTex(r"\mathrm{e}^{i(\alpha - \beta)} = \mathrm{e}^{i(\alpha)} + \mathrm{e}^{i(\text-\beta)}").next_to(euler, DOWN)
        diff_2 = MathTex(r"\cos(\alpha - \beta) + i\sin(\alpha - \beta) = (\cos \alpha + i\sin\alpha)(\cos \text-\beta + i\sin\text-\beta)").next_to(diff_1, DOWN)
        diff_3 = MathTex(r"\cos(\alpha - \beta) + i\sin(\alpha - \beta) = \cos \alpha \cdot\cos \text-\beta + \cos \alpha\cdot i\sin\text-\beta + i\sin\alpha\cdot\cos\text-\beta - \sin\alpha\cdot\sin\text-\beta").next_to(diff_2, DOWN)
        diff_sin_ident_with_i = MathTex(r"i\sin(\alpha - \beta) = i \sin\alpha\cdot\cos\text-\beta + i\sin\text-\beta\cdot\cos\alpha").next_to(diff_3, DOWN)
        diff_sin_ident_without_i = MathTex(r"\sin(\alpha + \beta) = \sin\alpha\cdot\cos\beta + \cos\alpha\cdot\sin\beta").next_to(diff_sin_ident_with_i, DOWN)
        diff_cos_ident = MathTex(r"\cos(\alpha - \bedta) = \cos \alpha \cdot \cos\beta + \sin \alpha \cdot \sin \beta").next_to(diff_sin_ident_without_i, DOWN)

        #Double Angle Identities
        double_1 = MathTex(r"\mathrm{e}^{i(\alpha + \alpha)} = \mathrm{e}^{i(\alpha)} + \mathrm{e}^{i(\alpha)}").next_to(euler, DOWN)
        double_2 = MathTex(r"\cos(\alpha + \alpha) + i\sin(\alpha + \alpha) = (\cos \alpha + i\sin\alpha)(\cos \alpha + i\sin\alpha)").next_to(double_1, DOWN)    
        double_3 = MathTex(r"\cos(\alpha + \alpha) + i\sin(\alpha + \alpha) = \cos^{2}\alpha + 2\cdoti\sin\alpha\cos\alpha - \sin^{2}\alpha)").next_to(double_2, DOWN)
        double_sin_ident_with_i = MathTex(r"i\sin(2\alpha) = 2\cdoti\sin\alpha\cos\alpha)").next_to(double_3, DOWN)
        double_sin_ident_without_i = MathTex(r"\sin(2\alpha) = 2\cdot\sin\alpha\cos\alpha)").next_to(double_sin_ident_with_i, DOWN)
        double_cos_ident_1 = MathTex(r"\cos(2\alpha) = \cos^{2}\alpha - \sin^{2}\alpha)").next_to(double_sin_ident_without_i, DOWN)
        double_cos_ident_2_a = MathTex(r"\cos(2\alpha) = (1-\sin^{2}\alpha) - \sin^{2}\alpha)").next_to(double_cos_ident_1, DOWN)
        double_cos_ident_2_b = MathTex(r"\cos(2\alpha) = (1-2\sin^{2}\alpha)").next_to(double_cos_ident_2_a, DOWN)
        double_cos_ident_3_a = MathTex(r"\cos(2\alpha) = \cos^{2}\alpha) - (1 - \cos^{2}\alpha)").next_to(double_cos_ident_2_a, DOWN)
        double_cos_ident_3_b = MathTex(r"\cos(2\alpha) = 2\cos^{2}\alpha-1)").next_to(double_cos_ident_2_b, DOWN)


        #self.add(euler, sum_1, sum_2, sum_3, sum_sin_ident_with_i, sum_sin_ident_without_i, sum_cos_ident)
        #self.add(euler, diff_1, diff_2, diff_3, diff_sin_ident_with_i, diff_sin_ident_without_i, diff_cos_ident)
        self.add(euler, double_1, double_2, double_3, double_sin_ident_with_i, double_sin_ident_without_i, double_cos_ident_1, double_cos_ident_2_a, double_cos_ident_2_b, double_cos_ident_3_a, double_cos_ident_3_b)
        self.wait(3)

  