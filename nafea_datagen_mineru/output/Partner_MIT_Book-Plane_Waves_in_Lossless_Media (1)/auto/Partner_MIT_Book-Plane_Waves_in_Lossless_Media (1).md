# Plane Waves in Lossless Media  

Our study of waves has been limited so far to those depending upon only one space dimcnsion.  1\1ost of the fielu aspects of the problem have been suppresseu by our use of the voltage anu current concepts. It is now our task to consider waves in more than one space dimension, and to pay more attention to the fields.  

The 1miform plane wave proviues a simple and important special case of wave motion in space, at the same time retaining, from one point of view, many featurcs charactcristic of transmission-line waves. From another point of view, hO\yever, uniform plane "'aves lead to a consiueration of the more general nonuniform plane ,,'aves, and to the whole question of guideu waves.  

The subject of plane waves is simplest whcn the medium in ,,,hich they propagate is lossless.  We treat this case in the present chapter, and the effects of loss in the next.  

# 7.1 Uniform Plane Waves in the Time Domain  

# 7.1.1 Introduction  

In Chapter 2, we encountered time-varying solutions of l\Iaxwell's equations with electric and magnetic fielus, each having only two eomponcnts.  These solutions are in a class we shall subsequently examine  further,  called  TE:\I  waves  (transverse  electromagnetic waves) , so nameu because the fielu vectors lie completely in planes transverse to the direction of wa"e propagation.  In Chapter 2, Sec. 2.3, moreover, ,,'e used the simplest form of such TE:\I ,,'aves to meet the bounuary conditions imposed by parallel, perfectly conducting planes.  This solution had the second special property that, at any instant of time, neither $\pmb{E}$ nor $\pmb{U}$ varied u'ith position in the transverse plane containing them.  This type of solution is known as a uniform plane wave (or sometimes an infinite plane mwe) .  It will be compared bter "'ith other TE:\I waves-like those on an open-wire line-in ,,"hich the strength and direction of $\pmb{E}$ and $\pmb{U}$ do vary with position in the transverse planes containing them (see Chapter l)).  

In the solution in Chapter 2, the direction of $\pmb{{\cal E}}$ in space ,yus chosen normal to the metal planes to meet the boundary conditions they im­ posed.  However, it is clear that, if the planes ,,'ere drawn apart in­ definitely, the entire field in space would remain a solution to Maxwell's equations.  Similarly, a uniform plane wave propagating in any direc­ tion in free space is also a solution of 1\Iaxwell's equations, inasmuch as the direction of propagation may always be taken as the $\textit{\textbf{z}}$ -axis to conform with our previous results.  

![](images/991b37dc080fc7a2f1f7a7f4d40a6584147f6c6c09a5d6adab3c803b7e481375.jpg)  
Fig.7.1.  Schematic pictures of two independent uniform plane waves propagating in the $+z$ direction.  

Since 1\IaxweII's equations, as ,,'e have agreed to consider them, arc linear vector equations, any sum of vector solutions is also a solution. Therefore a superpo:-;ition of many uniform plane waves traveling in different directions in space is a valid electromagnetic fieh!.  l\Ioreover, it is apparent that one uniform plane wave cannot be obtained as a linear combination of others propagating in different directions.  lIenee there are at least as many linearly independent uniform plane wave solutions to the field equations as there are different directions in space. 1\10re than this, even for a given direction of propagation, there are two linearly  independent  uniform  plane-wa"e  solutions  to  l\Iaxwell's equations.  Figure 7.1 and the following discussion are addressed to this matter.  

# 306  ELECTROMAGNETIC ENERGY TRANSMISSION AND RADIATION  

# 7.1.2  Details of the Solution  

In terms of the coordinate system of Fig. $7.1l)$ , \\"e shall write Max­ \\"ell's equations CEqs. $1.2{\cdot}4b$ , 1.23, and 1.31) for a lossless, linear, homo­ geneous medium "'ith consinnt parameters $\left(\sigma\equiv0,\;\epsilon,\;\mu\right)$ and without sources.  "r e shall cOllsider the case of uniform plane ,neves, for which, by our definition,  

$$
\begin{array}{c}{{E_{z}=I I_{z}=0}}\\ {{\displaystyle\frac{\partial}{\partial x}\equiv\frac{\partial}{\partial y}\equiv0}}\end{array}
$$  

There remain only the following equations, rearranged for convenience  

$$
\begin{array}{r l}&{\displaystyle\frac{\partial E_{x}}{\partial z}=\left.-\mu\,\frac{\partial I I_{y}}{\partial t}\right|_{\mathrm{Sct\,1}}\qquad\mathrm{(c)}\quad\frac{\partial E_{y}}{\partial z}=\left.\mu\,\frac{\partial I I_{x}}{\partial t}\right|_{\mathrm{Sct\,2}}}\\ &{\displaystyle\frac{\partial I I_{y}}{\partial z}=\left.-\epsilon\,\frac{\partial E_{x}}{\partial t}\right|^{\mathrm{Sct\,1}}\qquad\mathrm{(d)}\quad\frac{\partial I I_{x}}{\partial z}=\left.\epsilon\,\frac{\partial E_{y}}{\partial t}\right|^{\mathrm{Sct\,2}}}\end{array}
$$  

There are two irulependcnt pairs of equations: equations ${\bf7.2}a$ and ${}^{7.2b}$ relate only $\mathit{{E}}_{\mathbf{z}}$ and $\boldsymbol{I}\boldsymbol{I}_{y},$ whereas Errs. ${\mathbf{7.2}}c$ and $\mathbf{7.2}d$ relate only $E_{y}$ and $I I_{x}$ .  Each pair is formally identical "'ith the equations of a lossless transmission line.  The solutions can be written immediately.  

For Eqs. ${\bf7.2}a$ and ${}^{7.2b}$ , aside from the obvious d-c solutions, we have  

$$
\begin{array}{l}{{E_{x}=f_{+}\left(t-\frac{z}{v}\right)+f_{-}\left(t+\frac{z}{v}\right)}}\\ {{{\cal I}\!\!I_{y}=\displaystyle\frac{1}{\eta}\left[f_{+}\left(t-\frac{z}{v}\right)-f_{-}\left(t+\frac{z}{v}\right)\right]}}\end{array}
$$  

where  

$$
\eta=+{\sqrt{\frac{\mu}{\epsilon}}}\equiv{\mathrm{characteristic~wave~impcdance~(ohms)}}
$$  

$$
v={\frac{1}{+{\sqrt{\epsilon\mu}}}}\equiv{\mathrm{velocity~of~light}}
$$  

Considering the $(+)$ and $(-)$ waves separately, we have  

$$
\begin{array}{l}{{E_{x}^{\ +}=\,\eta I I_{y}^{\ +}=f_{+}\left(t-\frac{z}{v}\right)}}\\ {{\ }}\\ {{E_{x}^{\ -}=\ -\eta I I_{y}^{\ -}=f_{-}\left(t+\frac{z}{v}\right)}}\end{array}
$$  

If subscript 1 is uscu to uCllote the solution of Eq. 7.2, Set 1, we have  

$$
\begin{array}{l}{{E_{1}=a_{x}E_{x}=a_{x}{E_{x}}^{+}+a_{x}{E_{x}}^{-}=E_{1}{}^{+}+E_{1}{}^{-}}}\\ {{{}}}\\ {{I I_{1}=a_{y}I I_{y}=a_{y}I I_{y}{}^{+}+a_{y}I I_{y}{}^{-}=I I_{1}{}^{+}+I I_{1}{}^{-}}}\end{array}
$$  

Equations 7.5 become  

$$
\begin{array}{l}{{{\cal E}_{1}{}^{+}=\eta{\cal I}{\cal I}_{1}^{\ +}\,\times\,a_{z}}}\\ {{{\cal E}_{1}{}^{-}=\ -\eta{\cal I}{\cal I}_{1}^{\ -}\,\times\,a_{z}}}\end{array}
$$  

Equatioll $7.{\bar{\mathrm{o}}}a$ i:-; rl'pre:'mLcd sdlCmalienlly by Fig. 7.1e, in \\"hich the dotted line show:,; the directioll of propagation $(+z)$ .  

For Eqs. $\mathbf{7.2c}$ and ${}^{7}.2\d\ell$ ,  the ob viou:,; mouification of algebraic sign yiellls  

$$
\begin{array}{l}{{E_{y}=g_{+}\left(t-\frac{z}{v}\right)+g_{-}\left(t+\frac{z}{v}\right)}}\\ {{{}}}\\ {{I I_{x}=\mathrm{}-\frac{1}{\eta}\left[g_{+}\left(t-\frac{z}{v}\right)-g_{-}\left(t+\frac{z}{v}\right)\right]}}\end{array}
$$  

The fUlldiolls $g_{\pm}$ arc ill no \ray related to the functions $f_{\pm}$ in Eq:,;. 7.3 as far a:,; Eqs. 7.2 arc COiIlTl'llcd, becausc Eqs. $7.2c$ ::tnu $\mathbf{7.2}d$ are com­ pletely indepcndcllt of Eq:,;. $\mathbf{\nabla}7.2a$ am1 $7.2\6$ .  In place of Eqs. 7.5, we nOW ha\'c  

$$
\begin{array}{l}{{E_{y}^{\ +}=\,-\eta I I_{x}^{\ +}=\,g_{+}\bigg(\ell-\frac{z}{v}\bigg)}}\\ {{\ }}\\ {{E_{y}^{\ -}=\,\eta I I_{x}^{\ -}=\,g_{-}\bigg(\ell+\frac{z}{v}\bigg)}}\end{array}
$$  

If subscript 2 is used to dcnote the solution of Eq. 7.2, Set 2, we have  

$$
\begin{array}{l}{{E_{2}=a_{y}k_{y}^{\prime}=a_{y}k_{y}^{\prime}{}^{+}+a_{y}k_{y}^{\prime}{}^{-}=E_{2}{}^{+}+E_{2}{}^{-}}}\\ {{{}}}\\ {{I I_{2}=a_{x}I I_{x}=a_{x}I I_{x}{}^{+}+a_{x}I I_{x}{}^{-}=H_{2}{}^{+}+H_{2}{}^{-}}}\end{array}
$$  

Equations 7.0 become  

$$
\begin{array}{l}{{E_{2}^{\mathrm{~+~}}=\eta I I_{2}^{\mathrm{~+~}}\times\,a_{z}}}\\ {{{}}}\\ {{E_{2}^{\mathrm{~-~}}=\,-\eta I I_{2}^{\mathrm{~-~}}\times\,a_{z}}}\end{array}
$$  

Equation $7.9a$ is reprcscnted schematically by Fig. $7.1a$ .  

Equations 7.7 amI 7.11 prove that $\ensuremath{{\cal E}}_{1,2}^{\ensuremath{+},-},\,\ensuremath{{\cal I}}\ensuremath{{\cal I}}_{1,2}^{\ensuremath{+},-},$ , and the direc­ tion of propagation arc mutually perpcndicular for cach of the four  

separate waves.  Their relative orientations arc such that the Poynting vector $S_{1,2}^{+,-}$ is at every instant in the direction of propagation.  

$$
S_{1,2}{^+}\,=\,E_{1,2}{^+}\,\times\,I I_{1,2}{^+}\,=\,_{\eta}\vert\,I I_{1,2}{^+}\vert^{2}a_{z}\,=\,{\frac{1}{\eta}}\vert E_{1,2}{^+}\vert^{2}a_{z}
$$  

$$
S_{1,2}-\:=\:E_{1,2}-\:\times\:H_{1,2}-\:=\:-\eta\vert\,I\!\!I_{1,2}-\!\!\vert^{2}a_{z}\:=\:-\:\frac{1}{\eta}\vert\,E_{1,2}-\vert^{2}a_{z}\:\:
$$  

'Ve conclude that every uniform plane wave propagating in a given dircction (the $+z$ direction, for cxample) can always be decomposed into two waves having the same dircction of propagation but with mutually perpendicular electric (and magnetic) fielus.  Therefore any such solution ${{E}_{T}}^{+}$ and ${\pmb I}{\pmb I}_{T}{\pmb+}$ is expressible in the form  

$$
{E_{T}}^{+}={a_{x}}{E_{x}}^{+}+{a_{y}}{E_{y}}^{+}={E_{1}}^{+}+{E_{2}}^{+}
$$  

$$
I I_{T}^{\;+}=a_{y}I I_{y}^{\;+}+a_{x}I I_{x}^{\;+}=I I_{1}^{\;+}+I I_{2}^{\;+}
$$  

whcre the subscript $\pmb{T}$ stipulates that $\pmb{E}$ anu $\pmb{I}\pmb{I}$ lie in planes transverse to the direction of propagation.  A similar conclusion applies to $(-)$ waves.  

# 7.1 .3  Power Considerations and Orthogonality  

Having assured ourselves that every uniform plane wave may be ex­ pressed as a linear combination of the preceding four solutions, we must  now  consider some  gelleral properties of the energy  flow,  or Poynting vector, for such linear combinatiolls.  

First, the pmYer carried by the general $(+)$ "'ave (Eq. 7.13) is the algebraic sum of the $(+)$ wave powers carried by each component wave separately.  To prove this, note that  

$$
\begin{array}{c}{{S^{+}=E_{T}{}^{+}\,\times\,I I_{T}{}^{+}=\,(E_{1}{}^{+}+E_{2}{}^{+})\,\times\,(I I_{1}{}^{+}+I I_{2}{}^{+})}}\\ {{=E_{1}{}^{+}\,\times\,I I_{1}{}^{+}+E_{2}{}^{+}\,\times\,I I_{2}{}^{+}+E_{1}{}^{+}\,\times\,I I_{2}{}^{+}}}\\ {{+E_{2}{}^{+}\,\times\,I I_{1}{}^{+}}}\end{array}
$$  

But  

$$
E_{1}^{~+}\,\times\,H_{2}^{~+}=E_{2}^{~+}\,\times\,H_{1}^{~+}\equiv0
$$  

because ${E_{1}}^{+}$ and ${E_{2}}^{+}$ are parallel to ${H_{2}}^{+}$ and ${\pmb I}{\pmb I}_{1}^{+}$ respectively.  There­ fore, as stated above,  

$$
S^{+}=S_{1}{^+}+S_{2}{^+}
$$  

Similarly, for the $(-)$ waves:  

$$
S^{-}=S_{1}^{-}+S_{2}^{-}
$$  

The fact that the power in a $(+)$ [or $(-)]$ wave of Set 1 adds without cross terms to the power in a $(+)$ [or a $(-)]$ wave of Set 2, to give the total $(+)$ [or $(-)]$ \,·a ve power \r hen W[1, ves of Sets 1 and 2 arc present together, is one example of a more general condition known as ortho­ gonality of two solutions of a set of differential equations.  The usual statement of such a condition involves an integration.  For instance, suppose that in a region $R$ of space (or time) $\phi_{i}$ and $\phi_{j}$ arc two different scalar solutions of the same differential equation.  Then these functions arc said to be orthogonal if  

$$
\int_{R}\phi_{i}\phi_{j}\,d R=0\qquad\mathrm{~when~}i\not=j
$$  

If $\phi_{i}$ and $\phi_{j}$ arc vector functions, the mUltiplication under the integral \yould be either a dot- or cross-product.  Sometimes the integration need not eO\·er the whole region $R$ but may involve only a line or plane in it.  In the present case of uniform plane waves, the fields do not vary with position at all over planes normal to the direction of propaga­ tion.  Accordingly, a result like Eq. $7.13d$ may be integrated over any area in the plane of the fields.  Indeed, it may most conveniently be regarded as an orthogonality condition per unit area.  

As indicated above, the orthogonality of two functions makes sense only if they arc different.  By this, we mean that one is not simply a (nonzero) constant times the other $(\phi_{j}\neq a\phi_{i})$ . When they arc different in this sense, the functions arc said to be linearly independent.  Evi­ dently, orthogonality is not simply a consequence of the linear in­ dependence of the t,yO functions in question.  Additional conditions are necessary.  For example, in the present field problem, the solutions $E_{1}$ and $E_{2}$ arc orthogonal specifically because of their perpendicular rela­ tion in real space.  Such a relationship is by no means implied in the ,,·ord "orthogonality," as used in the general theory of orthogonal functions, and we shall shortly sec examples of orthogonality arising for quite difIerent reasons.  

To proceed still further with these ideas, consider the complete combination of $(+)$ and $(-)$ waves of Sets 1 and 2 (Eqs. 7.0 and 7.10). The Poynting vector is  

$$
\begin{array}{r l}&{S=(E_{1}+E_{2})\,\mathrm{~\times~}(I I_{1}+I I_{2})}\\ &{\quad=\,E_{1}\,\mathrm{~\times~}I I_{1}+E_{2}\,\mathrm{~\times~}I I_{2}+(E_{2}\,\mathrm{~\times~}I I_{1}+E_{1}\,\mathrm{~\times~}I I_{2})}\\ &{\quad=\,S_{1}+\,S_{2}+(E_{2}^{\mathrm{~+~}}\times\,I I_{1}^{\mathrm{~-~}}+E_{2}^{\mathrm{~-~}}\times\,I I_{1}^{\mathrm{~+~}}}\\ &{\qquad\quad\quad+E_{1}^{\mathrm{~+~}}\times\,I I_{2}^{\mathrm{~-~}}+E_{1}^{\mathrm{~-~}}\times\,I I_{2}^{\mathrm{~+~}})}\end{array}
$$  

in which we have already used Eq. $7.13d$ and its analog for $(-)$ waves.  

# 310  ELECTROMAGNETIC ENERGY TRANSMISSION AND RADIATION  

Once again, however,  

$$
{E_{2,1}}^{+}\,\mathrm{\boldmath~\times~}\,{H_{1,2}}^{-}=\,{E_{2,1}}^{-}\,\mathrm{\boldmath~\times~}\,{H_{1,2}}^{+}\equiv0
$$  

because ${E_{2,1}}^{+}$ amI ${E_{2,1}}^{-}$ arc parallel respectively to $I I_{1,2}-$ and ${{\cal I}}{{\cal I}_{1,2}}^{+}$ . It follows that the $(+)$ waves of one solution type arc orthogonal to the $(-)$ waves of the other and that  

$$
S=S_{1}+S_{2}
$$  

Finally, the similarity of ECJs. 7.3 and 7.S to those of a lossless trans­ mis;.;ion line reminds llS that the pO\rer carried hy comhine(I $(+)$ and $(-)$ wans of cit her Set 1 or Set 2 is al,.:o f'imply the algehraic sum of those carried scparately hy the $(+)$ and $(-)$ waves  t!one:  

$$
S_{1,2}\,=\,S_{1,2}^{\phantom{\dagger}}+\,S_{1,2}^{\phantom{\dagger}}-
$$  

although the reason for this fact is quite different from that underlying Eqs. 7.13c, 7.13], or 7.13i.  Here, imlced, "'e find an orthogonality relation between bro solutions having parallel electric fields!  

The net result of the power relations, Eqs. 7.13c, 7.13], 7.13£, and $7.13j$ , is that in [\, 10f'f'lef's, homogeneous, linear medium 'riih constant parametcrs the four possihle linearly independent uniform plane waves that h:n'e [\, common (undirected) axis of propagation (e.g"  the $\pm z-$ axis)  may ahrays be, amI  ha "e  here 1)('c1l,  cho;.;en  to be mulually orilw(fonal.  That is, the total pO\rer (per unit arca in this case) carried hy the field ,rhen all the ,,'aycs arc simultaneously present is simply the vector S11m of the po\rers that each would carry if it e xisted alone in space.  There arc JlO cross terms.  

# 7.1.4  Polarization  

We have found that "'aycs of Sets 1 amI 2 can al\\"ays be studied separately, not only in the light of normal superposition theory but abo in cOli]wetion 'rit h pO\rer.  It is no\\" appropriate to emphasize anot her char:H"tcristic of t hese waves \rhieh makes t hcm particularly easy to treat separ:1tdy: the space directions of $E_{1}$ (or $\ensuremath{\boldsymbol{E}}_{2}$ ) and $\pmb{I}\pmb{I}_{1}$ (or $\pmb{I}\pmb{I}_{2}^{\phantom{\dagger}}$ remain along fixl'd lines ill any tranS\'('l"!'e plane at all times.  Thus, as indicated hy Eqs. 7.G amI 7.3, $\pmb{{\cal E}}_{1}$ ah\-ays lies along a line parallel to the $x$ -axis.  It may reY('r!'e direetion along t his line as time progresses, depending upon the behavior of] $f_{+}$ and] $f_{-}$ ,  but no other change of direction O('curs.  Similar comments apply to $\pmb{{\cal I}}_{1},\ \pmb{{\cal E}}_{2}$ ,  and $\pmb{I}\pmb{I}_{2}$ •  To emphasize this behavior, the,",e wa,-es are referred to as being linrarly ]Jolarized.  In mo"t of the recent electrical engineering literature, the direction of polarization is taken to be that of $E$ ; so we shall say that lhe wave $(E_{1},\,H_{1})$ is linearly polarized in the $x$ -direction \yhilc $(E_{2},\,I I_{2})$ is lincarly polarized in the $\boldsymbol{y}$ -direction,  This situation is illuc;trated for the $(+)$ 'ntns by the sketchcs in Fi s. $7.1a$ and 7.le. $\Lambda$ similar picturc ,,"ould apply for $(-)$ \yan s.  For hoth to ethcr, the lincar polarization rcmains, but propa ation direction lo:::es meaning.  

The most general uniform plane-,,-ave propa ating in a ginll dircc­ tion is not linearly polarizcd.  Indced, Eqc;. $7.13a$ , $7.8a$ , amI $7.3a$ show that ${{\dot{E}}_{T}}^{+}$ has, in general, t,,-o spacc components in the transver"e planc, and that at any given point in space thcse components may be quitc different functions of the time. ${\it\Delta}\Lambda\mathrm{t}$ one moment $\boldsymbol{l}\boldsymbol{\xi}_{x}^{\dagger}{}^{+}$ might be Iar c and ${{\tilde{E_{y}}}^{+}}$ zero, \yhercns, at a later timc, ${{\mathrm{}}{{\mathrm{}}{\mathrm{}}}}{{\mathrm{}}}^{\prime}{{\mathrm{}}^{+}}$ might be largc and ${\mathit{L}}_{x}^{\prime}{}^{+}$ zcro.  Evidcntly the tip of the nctor ${\vec{E}}_{T}{}^{,+}$ traccs somc complicated path in the trans\-cr"e plane, just as thc spot On an oscilloscopc scrcen exccutcs an invoh"c(I pattern \yhen arbitrarily different voltage timc functions nrc impre"sed upon thc vertical and horizontal axes.  An cxtrcmc case of such eomplicate(I hehavior in clectromagnetic waves is that of "un polarized" light.  Its t,,-o  electric field  componcnts  are statistically imkpclllknt Gaus:-:ian random time funetiolls, \yith equal rms amplitudes amI zero averagc values.  Its polarization is thereforc "random," i.c., $E_{T}$ is at any instant as likely to be pointing in onc direc­ tion as another in thc transversc plane.l  Theref orc, in vic,,- of thc widc latitude of thc gcneral case, it is comforting to know that for cach dircction of propagation wc nccd con:::ider only two indcpcndcnt solu­ tions having mutually perpcndicular linear polarizations.  

# 7.1.5  Role of Uniform Plane Waves  

Since  the  ficlel of  a  uniform  plane W[l\'e  extcnds \yith  constant strength oycr the infinite arca of allY transvcrsc plane, the total pO\vcr carricd by such a wave is also infinite.  Thus no physical sourcc can po:::sibly bc cxpectcd to producc exactly such a wayc.  1\cverthelcss, wc shall find later, from our study of radiation, that at largc cnough distanccs from any physical sourcc thc field in suitably dcfined finite rcgions of space approximates c\o:)e\y  Umt of uniform planc \\"aves propagating ill appropriatc directions.  For this rcason and othcrs, a thorough understanding of these i:'implc \ya ves in spacc is fundamcntal to any study of e1cctromagnctic energy trani:'mission and radiation. There arc, hO\ye\"cr,  othcr simple solutions of l\Iaxwel\'s equations \vhich are cvcn more important, and it is not our intention to exclude them by this statement.  

,"Ve have shown on physical grounds that one or more uniform plane ,,'aves propagating in any direction or directions in free space con­ stitutes a solution of Maxwell's equations,  If we imagine one such wave propagating in the $+z$ direction, and r('gan! this as an incident ,,'ave produced by some remote source, "'e may a k the question: "What happens "'hen an object is placed in the path of this wave?" Unquestionably, the original wayc alone \\'ill rarely satisfy the bound­ ary conditions impo ed by the olJjeet.  The field iu the space about the object will almost surely be modified .  From our study of trans­ mission lines, \ye ha \'e lcal'llecl to interpret this modification as a "re­ flection" of some sort.  In this case, hO\\'eycr, the reflected field may or may not be another uniform plane wave.  Its nature depends en­ tirely upon the geometry and electrical character of the object.  

A perfectly conducting metal sphcre placed at $z\,=\,0$ may "scatter" the incident waye in all directions.  The reflected field would then be more properly described as a s-:?attered field, and it would not be :1 simple uniform plane W:1\'e.  

On the other hand, we should not be surprised to find that a smooth, infinite, pIane, perfectly conducting metal sheet placed normal to the direction of propagation will act like an optical mirror,  It will simply throw the incident ,,'aye back upon itself.  The reflected "Wie is then another uniform plane wave propagating in the opposite direction.  If this mirror is not normal to the direction of propagation of the incident waye, optical experience suggests that the reflected field should he another uniform plane wa ye \"ho;.:e direction of propaga tiou oheys the familar la \\': angle of reflection equals angle of incidence.  

When the ohject is a dielectric or a real metal rather than a perfect conductor, ,,'e expect to he concel'lled "'ith refraction as well as re­ flection, although, again, the question of whether or not the reflected and refracted fields arc simple uniform plane waves depends upon the shape and electrical character of the ohject.  

To soh'e the more elaborate among the types of problems described above, uniform plane waye solutions arc insufficient.  In the sinusoidal steady state or frequency domain, hmrever, it is not difIieult to find some more general plane wave solutions to :\Iax\\'ell's equat.ions.  These nrc called nonuniform plane zeaves in thi" book, although the nomen­ clature is not standard and perhaps not suffi cie ntly descriptive.  The important theoretical point about these solutions i:-1 that,  \rith the uniform plane waves we ha\'e already found, they sll./!icc to soh'c any steady-state field problem comprising regions of different linear, homo­ geneous,  isotropic,  time-invariant  materials.  Like  the  SillllCiOid  (or exponential) ill time, the::;e plane waves form a set of building blocks in space which may be combined by Fourier-integral methods to meet a wide selection of boundary conditions.  Although we will not consider elaborate problems here, it is obviously important to study carefully the character of both uniform and nonuniform plane waves in the sinusoidal steady state, and to apply them to the solution of some simple examples.  

Restriction to the sinusoidal steady state, of course, implies no loss of generality, in view of the normal Fourier-integral techniques for time functions.  

# 7.2 Plane Waves in the Sinusoidal Steady State and Frequency Domain  

As stated above, the nonuniform plane mLVe has significance only in the sinusoidal steady state or the frequency domain.  The uniform plane wa\'e, hO\\,eyer, has significance both in the time domain, as dis­ cussed in the preceding section, and in the frequency domain.  It is therefore advantngeous to begin our study of plane waves in the fre­ quency domain "'itll the uniform plane wave.  Our discussion of this subject is to be guided by the fact that we wish to go on into the more general case.  The treatment may therefore appear to be less direct than the topic of uniform plane waves itself would require.  

# 7.2.1  Uniform Plane W aves in the Frequency Domain  

7.2.1.1  Fom[ OF THE SOLUTIO:-r.  The formal similarity of Eqs. ${\bf7.2}a$ , 7.2/J, 7.3, and 7.-1 to those of a lossless transmission line tells us at once that the complex steady-state solution for $x$ -polarized uniform plane waves traveling in the $\pm z$ directions is  

$$
\begin{array}{r}{\mathrm{E}_{x}=\mathrm{E}_{x0}^{\phantom{}+}e^{-j\beta_{0}z}+\mathrm{E}_{x0}^{\phantom{}-}e^{j\beta_{0}z}}\end{array}
$$  

$$
\mathrm{II}_{\upsilon}=\frac{1}{\eta}\,(\mathrm{E}_{x0}+\!e^{-j\beta_{0}z}\,-\,\mathrm{E}_{x0}{}^{-}e^{j\beta_{0}z})
$$  

where  

$$
\beta_{0}\,=\,+\omega\sqrt{\epsilon\mu}
$$  

amI ${\mathrm{F}}_{x0}{}^{+}$ , $\mathrm{F}_{x0}-$ arc complex constants independent of $(x,\,y,\,z)$ .  For the $(+)$ wave, ${E_{x}}^{+}(=\mathrm{~Re~}[\mathrm{{E}}_{x0}{}^{+}e^{j(\omega t-\beta_{0}z)}])$ and $I I_{y}^{\ +}(=\mathrm{~Re~}[\mathrm{II}_{y0}^{\ +}e^{j(\omega t-\beta_{0}z)}]$ $=\operatorname{Re}\left[(\operatorname{E}_{x0}^{}^{+}/\eta)e^{j(\omega t-\beta_{0}z)}\right])$ arc in time phase and have the ratio $\pmb{\eta}$ at every point in space, and at every instant.  'Ye may wish to interpret the $(+)$ solution as an incident '\"aye and the $(-)$ one as n, reflected wave.  This interpretation certainly is yalid under appropriate bound­ ary conditions to ,rhidt "'c "'ill return in detail later.  Ko\\' we prefer to examine the solution it elf from another point of "iew.  

![](images/1b0a266f0bde7b23308fa05548ccc627005a3f44fad67430024521267baf1030.jpg)  
Fig. 7.2.  Rotation of coordinate axes.  

Consiller just the $(+)$ '\"aye in Eqs. 7.1·j and 7.];'), and suppose the axes $(x,\,y,\,z)$ u cd to describc it there arc not actually the ones "'c ,,-ish to usc in 0\11' problem.  Such n, situat.ion arises, for example, in describ­ ing simultaneou ly scn;raluniform plane '\"ayes propagating in different spacc directions.  Let us re Cl'Ye $(x,\,y,\,z)$ for the axes ,,-c really plan to use, and rewritc the $(+)$ ,r:n-e part of Eq. 7. H wit It new yariables $\left(x^{\prime},\,y^{\prime},\,z^{\prime}\right)$ substituted  for $(x,\,y,\,z)$ .  From  the point of yiew of thc $(x,\,y,\,z)$ coordinates, t.he $\left(x^{\prime},\,y^{\prime},\,z^{\prime}\right)$ axes arc thel l  :t ri!2;ht-handetI set of rotated axes having thc same ori!2;in as $(x,\,y,\,z)$ , Fig. 7.2, but ,ritIt thc $+x^{\prime}.$ -axis cho"cll parallel to thc (li nearly polarized) electric field yector of the $(+)$ ,,-ave of interest, alHI the $+z^{\prime}.$ -axis chosen parallel to the direction of propagation.  Thereforc  

$$
\begin{array}{l}{{\bf{E}}^{+}={a_{x}}{\mathrm{{E}}_{x^{\prime}0}}^{+}e^{-j{\beta_{0}}z^{\prime}}}\\ {\mathrm{{}}}\\ {{\bf{I I}}^{+}=\displaystyle\frac{1}{\eta}{a_{y}}{\mathrm{E}_{x^{\prime}0}}^{+}e^{-j{\beta_{0}}z^{\prime}}}\end{array}
$$  

With reference to Fig. 7.2 again, Irt the (real) direction cosines of axis $+z^{\prime}$ with respect to axes $(+x,+y,+z)$ respecti,-cly be $(l_{z},\,m_{z},\,n_{z},)$ ' Similarly, let $(l_{x^{\prime}},\,m_{x^{\prime}},\,n_{x^{\prime}})$ and $(l_{y^{\prime}},\,m_{y^{\prime}},\,n_{y^{\prime}})$ apply correspondingly to  

axes $+x^{\prime}$ amI $+y^{\prime}$ rc pectivcly.  Theil bccausc the axes $\left(x,\,y,\,z\right)$ are $\Omega$ rectangular set, ,YC havc for the $+z^{\prime}$ -axis direction co:sincs  

$$
{l_{z^{\prime}}}^{2}+{m_{z^{\prime}}}^{2}+{n_{z^{\prime}}}^{2}=1
$$  

Similar results for the $+x^{\prime}$ and $+y^{\prime}$ axes are obtaincd by simply replac­ ing $z^{\prime}$ with $x^{\prime}$ or $y^{\prime}$ .  

"·e wi:sh now to describe the field (Eq. 7.10) in terms of the $\left(x,\;y,\;z\right)$ coordinates and abo the unit vectors $\pmb{a}_{x},\pmb{a}_{y},\pmb{a}_{z}$ along the corresponding axes, whereas it is presently deserihed in the coordinates $(x^{\prime},\,y^{\prime},\,z^{\prime})$ all thc unit vector" $\displaystyle\mathbf{\langle}u_{x^{\prime}},\,\mathbf{\langle}u_{y^{\prime}},\,\mathbf{\langle}u_{z^{\prime}}$ along them.  

To this elHI ,YC note first that thc position of any point in space is gi\'cn by its vcctor disphu:('mellt $\pmb{r}$ from the origin, all(l that thi::: same vee tor i" expre:::siblc ill t,\"o "'ays, cOlTespolHlillg to the t,\"o :::cis of axe".  

$$
r=a_{x}x+a_{y}y+a_{z}z=a_{x^{\prime}}x^{\prime}+a_{y^{\prime}}y^{\prime}+a_{z^{\prime}}z^{\prime}
$$  

Taking the dot product of both sides of Eq. 7.18 ,,"ith $\pmb{a}_{\pmb{z}^{\prime}}$ , and noting that axes $(x^{\prime},\,y^{\prime},\,z^{\prime})$ nrc a reetangubr set, we find  

$$
z^{\prime}=l_{z^{\prime}}x+m_{z^{\prime}}y+n_{z^{\prime}}z
$$  

Therefore the phase factor $\beta_{0}z^{\prime}$ in Eq. 7.1G becomes  

$$
\begin{array}{r l}&{\beta_{0}z^{\prime}\,=\,(\beta_{0}l_{z^{\prime}})x\,+\,(\beta_{0}m_{z^{\prime}})y\,+\,(\beta_{0}n_{z^{\prime}})z}\\ &{~~~~~~=\,{\upbeta}\cdot{\pmb r}}\end{array}
$$  

with  

$$
\begin{array}{r l}&{\upbeta=a_{x}(\beta_{0}l_{z^{\prime}})+a_{y}(\beta_{0}m_{z^{\prime}})+a_{z}(\beta_{0}n_{z^{\prime}})}\\ &{\quad=a_{x}\beta_{x}+a_{y}\beta_{y}+a_{z}\beta_{z}}\end{array}
$$  

where  

$$
\beta_{x}\,=\,\beta_{0}l_{z},\qquad\beta_{y}\,=\,\beta_{0}m_{z},\qquad\beta_{z}\,=\,\beta_{0}n_{z},
$$  

and  

$$
\mathfrak{B}\cdot\mathfrak{B}\equiv|\mathfrak{B}|^{2}=\beta_{0}{}^{2}(l_{z^{\prime}}{}^{2}+m_{z^{\prime}}{}^{2}+n_{z^{\prime}}{}^{2})=\beta_{x}{}^{2}+\beta_{y}{}^{2}+\beta_{z}{}^{2}=\beta_{0}{}^{2}
$$  

The IJ7"Opagation vee/or $\upbeta$ i" ill thi" case a real space ,"ector, ,yho:-;c (lircc­ tion is (hat of thc propa1!:atioll of the ,rave amI ,yho:-;e magnitude is thc phase eOIl"tall t $\beta_{0}\,=\,\omega{\sqrt{\epsilon\mu}}$ .;  

Kext, from the geometry of Fig. 7.2 we note that  

$$
\begin{array}{r}{a_{x^{\prime}}=a_{x}l_{x^{\prime}}+a_{y}m_{x^{\prime}}+a_{z}n_{x^{\prime}}}\end{array}
$$  

Consequently  

$$
\begin{array}{r}{a_{x^{\prime}}\mathrm{E}_{x^{\prime}0}{}^{+}=a_{x}l_{x^{\prime}}\mathrm{E}_{x^{\prime}0}{}^{+}+a_{y}m_{x^{\prime}}\mathrm{E}_{x^{\prime}0}{}^{+}+a_{z}n_{x^{\prime}}\mathrm{E}_{x^{\prime}0}{}^{+}}\\ {=\mathrm{E}_{0}{}^{+}\qquad\qquad\qquad\qquad\qquad\qquad\quad}\end{array}
$$  

where ${\bf E}_{0}{}^{+}$ is a complex vector independent of $(x,y,z)$ .  

# 316  ELECTROMAGNETIC ENERGY TRANSMISSION AND RADIATION  

From Eqs. ${\bf7.24a}$ and ${\bf7.21a}$ we find  

$$
\beta\cdot{\bf E}_{0}^{+}=\beta_{0}\mathrm{E}_{x^{\prime}0}^{\phantom{+}}+(l_{x^{\prime}}l_{z^{\prime}}+m_{x^{\prime}}m_{z^{\prime}}+n_{x^{\prime}}n_{z^{\prime}})\,=\,0\,=\,\upbeta\cdot{\bf E}^{+}
$$  

since the $x^{\prime}.$ - and $z^{\prime}.$ - axes arc perpendicular.  The meaning of Eq. $7.24l)$ is that the instantaneous electric field $\pmb{{\cal E}}^{+}(t)$ is at all times perpcndicular to the direction of propagation ; but this cOll('lu i()n is lc s obvious from Eq. $7.24\time10$ than it may appear offhand.  In gCllcral, the nllli hing of the dot product of two complex ,"cctors docs not imply allY  imple perpendicular condition in Teal  pace.  In 1-:q. $7.2.1\,l)$ , howenr, ${\upbeta}$ is a Teal vector, so $\boldsymbol{\upbeta}\mathbf{\cdot}\mathbf{I}\dot{\boldsymbol{\\\upvarepsilon}}^{+}=0$ ollly occurs if $\beta\!\cdot\!\mathrm{I}\!:\!\mathrm{e}\;\mathbf{I}\!:^{+}=0$ and $\boldsymbol{\upbeta}\cdot\mathrm{Im}~\mathbf{I}\boldsymbol{\updownarrow}^{+}=$ O.  Since He $\mathrm{E^{+}}$ and $\operatorname{Im}\,\operatorname{F}^{+}$ determine the plane in which $E^{+}(t)$ lics at all times (Sec. 1.2.2.1), ${\upbeta}$ is indeed perpendicular to this plane Hnti, therefore, to ${\pmb{\cal E}}^{+}(t)$ .  Of course, this perpendicular relation was true of the original field (Eq. 7.1G), and the use of new axes $\left(x,y,z\right)$ could hardly  be expected to alter it.  1\ e\'erthcless, the point about in­ terpreting Eq. $7.2.4b$ is important for our later work.  

In connection with the magnetic field  (Eq. 7. 1Gb), we note that $(x^{\prime},\,y^{\prime},\,z^{\prime})$ is a right-handcd set of rectangular axes like $(x,\,y,\,z)$ .  There­ fore  

$$
\begin{array}{r l}&{a_{y^{\prime}}\mathrm{E}_{x^{\prime}0}^{\mathrm{~\,~A~}}=(a_{z^{\prime}}\times\,a_{x^{\prime}})\mathrm{E}_{x^{\prime}0}^{\mathrm{~\,~A~}}=a_{z^{\prime}}\,\mathrm{~\times~}(a_{x^{\prime}}\mathrm{E}_{x^{\prime}0}^{\mathrm{~\,~A~}})}\\ &{\qquad\qquad=a_{z^{\prime}}\,\mathrm{~\times~}\mathrm{E}_{0}^{\mathrm{~\,~A~}}=(a_{x}l_{z^{\prime}}+a_{y}m_{z^{\prime}}+a_{z}n_{z^{\prime}})\,\mathrm{~\times~}\mathrm{E}_{0}^{\mathrm{~\,~A~}}}\\ &{\qquad\qquad=\frac{8}{\beta_{0}}\times\mathrm{~\mathrm{E}_{0}^{\mathrm{~\,~A~}}}}\end{array}
$$  

where \\'e have also used Eqs. $\mathbf{7.2.1}a$ and $7.21a$ .  

In summary, the solution (ECI. 7.1G) in the $(x,\,y,\,z)$ axis system be­ comes:  

$$
\begin{array}{l}{{\bf{E}}^{+}=\frac{\mathrm{{\bf~E}}_{0}+_{e}-j\beta\cdot\tau}{\omega}=\mathrm{{\bf~E}}_{0}+_{e}-j\beta_{x}x_{e}-j\beta_{y}y_{e}-j\beta_{z}z}\\ {{\bf{I}}\mathbf{I}^{+}=\frac{\beta\ \times\mathrm{{\bf~E}}^{+}}{\omega\mu}}\end{array}
$$  

The fact that $\upbeta$ is real allo\\'s us to interpret Eqs. $7.2\#b$ and 7.2Gb as show­ ing the mutual perpcndic'ularity of $\beta,H^{+}(t)$ , and $E^{+}(i)$ , by the same kind of argument \\'hic'h followed Eq. 7.2Ib.  

Obsen'e from Eq. $7.2.1a$ that ${\bf{{F}}}_{0}{}^{+}$ in Eq. 7.2G has three spaee com­ ponents in the $(x,\,y,\,z)$ sy"tcm.  They all have the same time-phase angle in the pre"cnt ca;<c hccause $l_{x^{\prime}},\,\d{\mathcal{W}}_{x^{\prime}},$ $n_{x^{\prime}}$ are real llllmhers.  Hellce, as \\'e expect, rotation of the coordinates has not altered the lineal' polarization of the wayc (Eq. 7.W) .   It is \\'orth remarking here, how­ ever, that we may also consider the second type of polarization in the $(x^{\prime},\,y^{\prime},\,z^{\prime})$ system, for \yhieh the complex steacly-state solution comes from Eq. 7.8 in the form $\ensuremath{{\mathbf{E}}_{2}}^{+}=\ensuremath{{\mathbf{a}}_{y^{\prime}}}\ensuremath{\mathrm{{F}}_{y^{\prime}0}}^{+}e^{-j\beta_{0}z^{\prime}}$ .  If we combine the t,,·o fields to make $\mathrm{E_{3}}^{+}=(a_{x},\mathrm{F}_{x^{\prime}0}{}^{+}+a_{y},\mathrm{F}_{y^{\prime}0})e^{-j\beta_{0}z^{\prime}}$ , the result in the $(x,\,y,\,z)$ system is again  of the form $\mathbf{E}_{3}^{\scriptscriptstyle+}=\mathbf{E}_{03}^{\scriptscriptstyle+}e^{-j\mathsf{B}\cdot\pmb{r}}$ .  This time, though,  

$$
\begin{array}{r l r}{\mathrm{E}_{03}^{\mathrm{{+}}}=\,a_{x}(l_{x^{\prime}}\mathrm{E}_{x^{\prime}0}^{\phantom{x^{\prime}}+}+l_{y^{\prime}}\mathrm{E}_{y^{\prime}0}^{\phantom{x^{\prime}}+})+a_{y}(m_{x^{\prime}}\mathrm{E}_{x^{\prime}0}^{\phantom{x^{\prime}}+}+m_{y^{\prime}}\mathrm{E}_{y^{\prime}0}^{\phantom{x^{\prime}}+})\,}&{{}}&{}\\ {+\,a_{z}(n_{x^{\prime}}\mathrm{E}_{x^{\prime}0}^{\phantom{x^{\prime}}+}+n_{y^{\prime}}\mathrm{E}_{y^{\prime}0}^{\phantom{x^{\prime}}+})\,,\,}\end{array}
$$  

"'here the three space components do not, in general, have the same time phase .  The point is: Eq. 7.2G is valid \yhether or not the uniform plane wave in question is linearly polarized.  Consequently,  the mutual perpendicularity of $\mathbf{\lambda}3,\mathbf{\,}\pi^{+}(t)$ , ami $E^{+}(t)$ remains true regardless of the type of polarization il1\·o!\·ecl.  

7.2.1.2  PUASJ';, "rAVE LEXGTH, AND PlIASg VELOCITY.  From Eq. 7.2G, we learn that the time phase of the electric (or magnetie) field varies with pO!'ition only as ${\upbeta}\cdot{\v r}$ .  ""ith reference to Fig. $7.3a$ , n. surJace oj constant phase is therefore one for which  

$$
\upbeta{\cdot}r\,=\,\mathrm{const}=\,\beta_{0}r\,\cos\psi
$$  

$$
r\cos\psi=\mathrm{const}
$$  

where $\scriptstyle{r}\;=\;\left\lfloor{r}\right\rfloor$ .  Equation $7.27\!\!\!/$ restricts $\pmb{r}$ to those points in space where its projection along the direction of $\upbeta$ is a constant.  The tip of $\pmb{r}$ must therefore lie in u plane perpendicular to $\upbeta$ .  Such planes, normal to the propagation direction, are the IJZanCS oj constant phase.  For the tmiJunn plane "'ave, they are also planes oj constant magnitude since ${{\bf{E}}_{0}}^{+}$ does not vary with position.  The electric and magnetie fields lie in these planes (Eqs. $7.2\mathrm{{+}}1\mathrm{{/}}\rangle$ and 7.2Gb).  

The direction normal to the planes of constant phase is the one in  

![](images/7c707e46729550454dd3af2260971607ac50b1c7d44eba93815457984eaf88c4.jpg)  
Fig. 7.30.  Equiphase surface for a plane wave.  

# 318  ELECTROMAGNETIC ENERGY TRANSMISSION AND RADIATION  

which the phase $\varphi$ of the field changes most rapidly with position.  To see this, we \Yl'ite with reference to EC[s. $7.20a$ , 7.27, anel Fig. $7.3a$ ,  

$$
{\begin{array}{r l}{\varphi=\upbeta\cdot r+\mathrm{const}\ \,}&{}\\ {\left({\frac{\partial\varphi}{\partial r}}\right)_{\psi=\mathrm{const}}=\beta_{0}\,\mathrm{cos}\,\psi}\\ {\left({\frac{\partial\varphi}{\partial r}}\right)_{\mathrm{max}}}&{=\left.+\beta_{0}\ \ \ }&{\mathrm{for}\,\psi=0,\,\mathrm{or}\,r\,\Vert\upbeta\Vert}\\ {\mathbf{vs}\,\psi}\end{array}}
$$  

Hence another d rscript ion of the propagation YCctor ${\upbeta}$ of a uniform plane wave in a IOf'slcf's medium is a.-ector who;;c direction is that of the maximum ratc-of-ehanp.;e of phase with po:-ition, and \\"I1O::;e magni­ tude $\beta_{0}$ equals that maximum rate of change.  In other words, by de­ finition of the gradient operator,  

$$
\nabla\varphi=\upbeta=a_{x}\beta_{x}+a_{y}\beta_{y}+a_{x}\beta_{z}\qquad\mathrm{~for~a~uniform~plane~wave}\quad(7\
$$  

The meaning of the component phase constants $\beta_{x},\,\beta_{y},$ and $\beta_{z}$ is the space-rate-of-eh:lI1ge of pha:-e as mea::;urc(l along the respective axes. According to Eqs. ${\bf7}.21a$ amI 7.28,  

so  

$$
{\begin{array}{r l}&{\varphi=\beta_{x}x+\beta_{u}y+}\\ &{\beta_{x}=a_{x}\cdot\nabla\varphi={\frac{\partial\varphi}{\partial x}}}\\ &{\qquad\beta_{y}=a_{y}\cdot\nabla\varphi={\frac{\partial\varphi}{\partial y}}}\\ &{\beta_{z}=a_{z}\cdot\nabla\varphi={\frac{\partial\varphi}{\partial z}}}\end{array}}
$$  

Observe that since the direction eo;;incs $l,\,m$ , and $^n$ cannot exceed 1 in magnitude (also in .-iew of EC[. 7.22),  

$$
|\beta_{x,y,z}|\,\le\beta_{0}
$$  

Insica(l  of  considering  the  space-rate-of-ehange  of  pha::;e  along various directions, \\'e can con:-ider the distanC'es between successive equipha;;e  surfaces  on  \\'hiC'h  the  field pha:-e differs by  exactly $2\pi$ . The;;e distanC'cs \\·ill be alJTJaI'Cllt 1Cnt'C [clluths beeause the phase shift is linearly proportional to di;;tance in any direction.   reasured along the propagation direction  (Fig. 7.3/1), the di;;tance $\lambda$ , in which the phase changc;; by $2\pi$ l', is the ('Oll\'cntion:d \\,:t\'(  length.  l\Ieasure<! along any other direc·t ion,  the di"t:I1H'CS hetm'en the ::;ame t\\·o planes will  be (If('afel' thall $\uplambda$ , as  "h()\\"11 ill Fig;. $7.3l)$ , ],('c':\use the space-rate-of-eh:lIlge of ph:1H  along; such a dire(·j iOIl is les8 thall it is along the propagation Jirl'clioll.  Thus  

![](images/dcd860ad039b995d6e06d7788aea4a14a0f43a02c7c4e54a657b0c8171bc7f21.jpg)  
Fig.7.3b.  Various wave-length concepts for a plane wave.  

$$
\begin{array}{l}{\lambda=\frac{2\pi}{\beta}}\\ {\ }\\ {\lambda_{x}=\frac{2\pi}{|\beta_{x}|}\geq\lambda}\\ {\ }\\ {\lambda_{y}=\frac{2\pi}{|\beta_{y}|}\geq\lambda}\\ {\ }\\ {\lambda_{z}=\frac{2\pi}{|\beta_{z}|}\geq\lambda}\end{array}
$$  

ancl, in vic\\' of Eqs. 7.22 and 7.33,  

$$
\frac{1}{{\lambda_{x}}^{2}}+\frac{1}{{\lambda_{y}}^{2}}+\frac{1}{{\lambda_{z}}^{2}}=\frac{1}{\lambda^{2}}
$$  

Similarly, sillce in the j imc clomaill (for the sinusoidal ::;teady state) $\mathrm{^a}$ particular plla"e front (pbne) mo\"('s ulliformly with time at speed $v\,=\,1/\sqrt{\epsilon\mu}\,=\,\omega/\beta_{0}$ along the propagatioll dirl'<'Iion, its intercept along any oj her din'C'I ion al"o 11100·('S uniformly ,\"it h time.  ;\s is slim\"!1 in  

Fig. $7.3\lambda$ , howenr, the apparent speed measured along any of the coordinate axes "'ill be greater than that along $\upbeta$ .  In the time of one cyele (1/f), a pha>:e front mons a di"tnnce along $\boldsymbol{x}$ of $2\pi/|\beta_{x}|\;=\;\lambda_{x},$ becau::e the total phase of the field invo!\'es $\omega t-\beta_{x}x$ .  Analogous com­ ments apply for the other directions $\mathcal{Y}$ , and $^z$ .  Thus the various ap­ parent phase velocities are $v_{x}=f\lambda_{x},$ etc.; or  

$$
v_{x}\equiv\frac{\omega}{\beta_{x}}=\left(\frac{1}{l_{z^{\prime}}\sqrt{\epsilon\mu}}\right)\geq v
$$  

$$
\begin{array}{l}{\displaystyle{v_{y}\equiv\frac{\omega}{\beta_{y}}=\left(\frac{1}{m_{z^{\prime}}\sqrt{\epsilon\mu}}\right)\geq v}}\\ {\displaystyle{v_{z}\equiv\frac{\omega}{\beta_{z}}=\left(\frac{1}{n_{z^{\prime}}\sqrt{\epsilon\mu}}\right)\geq v}}\end{array}
$$  

and in view of Eqs. 7.22, again  

$$
\frac{1}{{v_{x}}^{2}}+\frac{1}{{v_{y}}^{2}}+\frac{1}{{v_{z}}^{2}}=\frac{1}{v^{2}}=\epsilon\mu
$$  

There is a familiar analogy to the fact that the apparent wave length and phase velocity along any direction but that of the mwe propnga­ tion  exceed  the  same  quantities  along  the  propagation  direction. Visualize \\'ater waves striking a bcach obliquely.  The distance be­ tween su('('es;::ive crests, for example, i::; huge along the beach, especially if the ,,'aves arc only slightly ofT normal incidence.  Also to keep up \dth a given crest, one has to run much faster along the beach than the waves progress in their own normal direction.  

In view of the manner of obtaining the field expressions (Eqs. 7.26) and the auxiliary relations (Eq:;. 7.22 and 7.2-!b) by coordinate rotation from Eqs. 7.IG, there i:; no doubt that in the $(x,\,y,\,z)$ axes they con­ stitute a solution to ::\Iax\\'ell's (vector) equations.  The entire space depemlence of thi:; :;olution i:; a sill/pre e.1·poncntial, i.e., the exponent is linear in the variables $(x,\,y,\,z)$ .  There remains the question of whether or not \\'e have found the only such simple exponential solution to l\Iaxwell's equations in the sinusoidal steady state.  

# 7.2.2  Nonuniform Plane Waves \*  

7.2.2.1  CIL\HACTEH  OF  TIn;  SOLUTIO:--..r \*  The  most  general  ex­ ponential expres;::ions for the complex fields, \dth exponent linear in  

the variables $(x,y,z)$ , are of the form  

$$
\begin{array}{r l}&{\mathbf{E}=\mathbf{E}_{0}e^{-\bar{\gamma}_{x}x}e^{-\bar{\gamma}_{y}y}e^{-\bar{\gamma}_{z}z}\,=\mathbf{E}_{0}e^{-\bar{\mathbf{\gamma}}\cdot\mathbf{\bar{\mathbf{\gamma}}}\cdot\mathbf{\bar{\mathbf{\gamma}}}}}\\ &{\mathbf{H}=\mathbf{II}_{0}e^{-\bar{\gamma}_{x}x}e^{-\bar{\gamma}_{y}y}e^{-\bar{\gamma}_{z}z}=\mathbf{II}_{0}e^{-\bar{\mathbf{\gamma}}\cdot\mathbf{\bar{\mathbf{\gamma}}}\cdot\mathbf{\bar{\mathbf{\gamma}}}}}\end{array}
$$  

where $\mathbf{E}_{0}$ and $\mathbf{II}_{0}$ are constant complex vectors, independent of $(x,y,z)$ , and the various $\overrightharpoon{\gamma}^{\dag}$ s are complex numbers  

$$
\begin{array}{r}{\bar{\gamma}_{x}=\alpha_{x}+j\beta_{x}}\\ {\bar{\gamma}_{y}=\alpha_{y}+j\beta_{y}}\\ {\bar{\gamma}_{z}=\alpha_{z}+j\beta_{z}}\end{array}
$$  

The propagation vector $\bar{\pmb{\upgamma}}$ is then a complex vector  

$$
\begin{array}{c}{{\tilde{\mathbf{v}}=\,a_{x}\tilde{\gamma}_{x}+a_{y}\tilde{\gamma}_{y}+a_{z}\tilde{\gamma}_{z}=\,(a_{x}\alpha_{x}+a_{y}\alpha_{y}+a_{z}\alpha_{z})+j(a_{x}\beta_{x}}}\\ {{+a_{y}\beta_{y}+a_{z}\beta_{z})}}\\ {{=\,\alpha+j\mathfrak{b}}}\end{array}
$$  

$\pmb{\alpha}$ and $\upbeta$ being real space vectors.  We shall call $\pmb{\alpha}$ the attenuation vector and $\upbeta$ the phase vector.  With $\bar{\pmb{\upgamma}}$ complex, the field (L'q. 7.37) is by de­ finition a nonuniform plane wave.  

We know alreauy that if $\pmb{\alpha}=0$ the field of Eq. 7.37 can be a solution to l\laxwell's equations, provided $\mathrm{F}_{0},\,\mathrm{H}_{0}.$ , and ${\upbeta}$ satisfy some auxiliary conditions.  If they do,  the re::;ultillg solution  is interpretable as a uniform plane wave traveling in some arbitrary direction in space. If $\pmb{\alpha}\neq0$ , however, ,,·e must uetermine whether or not Eq. 7.37 can be a solution to the equations  

$$
\begin{array}{l}{{\nabla\,\times\,{\bf{E}}\,=\,-j\omega\mu{\bf{I I}}}}\\ {{\nabla\,\times\,{\bf{I I}}\,=\,j\omega\epsilon{\bf{E}}}}\end{array}
$$  

and, if so, how to interpret this solution.  

The first question above can be answereu by substituting Eqs. 7.37 into Eqs. 7.3\).  Expansion of the curl term in Eq. $7.39a$ yielus  

$$
\begin{array}{r l}&{\nabla\,\times\,{\bf E}=\nabla\,\mathrm{\boldmath~\times~}({\bf E}_{0}e^{-\hat{\mathrm{\boldmath~\scriptstyle7~}}\cdot r})\,=\,-{\bf E}_{0}\,\mathrm{\boldmath~\times~}\,\nabla e^{-\hat{\mathrm{\boldmath~\scriptstyle7~}}\cdot r}+e^{-\hat{\mathrm{\boldmath~\scriptstyle7~}}\cdot r}\,\nabla\,\mathrm{\boldmath~\times~}\,{\bf E}_{0}}\\ &{\qquad\quad=\,{\bf E}_{0}\,\mathrm{\boldmath~\times~}\,[e^{-\hat{\mathrm{\boldmath~\scriptstyle7~}}\cdot r}\,\nabla(\bar{\mathrm{\boldmath~\scriptstyle7~}}\cdot r)]\,=\,({\bf E}_{0}\,\mathrm{\boldmath~\times~}\,\bar{\mathrm{\boldmath~\scriptstyle7~}})e^{-\bar{\mathrm{\boldmath~\scriptstyle7~}}\cdot r}}\end{array}
$$  

because, since $\mathbf{E}_{0}$ is inuepenuent of $(x,\,y,\,z)$ , $\nabla\,\textbf{\times}\,\mathbf{E}_{0}\equiv0.$ . $\Lambda$ similar calculation is maue of $\nabla\,\textbf{\times}\,(\mathbf{I}\mathbf{I}_{0}e^{-\,\bar{\mathbf{v}}\cdot\boldsymbol{r}})$ .  Substitution of these results, with Eqs. 7.37, into Eq. 7.3U yields the final conuitions :  

$$
\begin{array}{r l}&{\bar{\texttt{Y}}\times{\texttt{E}}_{0}=j\omega\mu{\texttt{H}}_{0}}\\ &{\bar{\texttt{Y}}\times{\texttt{H}}_{0}=-j\omega\epsilon{\mathbb{E}}_{0}}\end{array}
$$  

# 322  ElECTROMAGNETIC ENERGY TRANSMISSION AND RADIATION  

It is clear that, if the exponential factors in E anu 11 hau been chosen unequal in Eq. 7.37, they woulu have been forceu to equality at this point for any solution to be possible.  Equations 7.40 result in any case.  

Now dot-premultiplying Eqs. $7.40a$ and $7.40b$ by $\bar{\mathfrak{Y}}$ , anu noting that  

$$
\bar{\Psi}^{*}(\bar{\Psi}\,\times\,{\bf E}_{0})\,=\,(\bar{\Psi}\,\times\,\bar{\Psi})^{*}{\bf E}_{0}\,=\,0\,=\,\bar{\Psi}^{*}(\bar{\Psi}\,\times\,{\bf I I}_{0})\,=\,(\bar{\Psi}\,\times\,\bar{\Psi})^{*}{\bf I I}_{0}
$$  

because  

$$
\bar{\texttt{y}}\times\bar{\texttt{Y}}\equiv0
$$  

we find  

$$
\begin{array}{l}{{\bar{\bf\Delta}}{\bar{\bf y}}{\bf\cdot}{\bf E}_{0}=0}\\ {{\bar{\bf\Delta}}{\bf\bar{y}}{\bf\cdot}{\bf I}{\bf I}_{0}=0}\end{array}
$$  

Since ${\bar{\mathbf{v}}},{\bar{\mathbf{r}}}_{0}.$ , and $\mathbf{I}\mathbf{I}_{0}$ arc complex vcdors in general, Eqs. 7.40 anu 7.41 do not imply any obvious conuitions of perpenuiculal'ity in spucc.  

To eliminate $\mathbf{I}\mathbf{I}_{0}$ from Eqs. 7.40, cross-premultiply Eq. $7.40a$ by $(\bar{\mathbf{v}}/\dot{\boldsymbol{\sigma}}\omega\boldsymbol{\mu})$ and auu Eqs. $7.40a$ anu 7.40b.  There results  

or  

$$
\begin{array}{c}{{\bar{{\bf\Delta}}\,{\bf\Delta}\times\,\left(\bar{{\bf\Delta}}\times{\bf\Delta}{\bf E}_{0}\right)\,=\,\omega^{2}\epsilon\mu{\bf E}_{0}\,=\,{\beta_{0}}^{2}{\bf E}_{0}}}\\ {{{}}}\\ {{\bar{{\bf\Delta}}(\bar{{\bf y}}\cdot{\bf E}_{0})\,-\,(\bar{{\bf y}}\cdot\bar{{\bf y}}){\bf E}_{0}\,=\,{\beta_{0}}^{2}{\bf E}_{0}}}\end{array}
$$  

In view of Eq. 7.-1 1a allll our \\'i"h to kl \'C $\mathbf{{F}}_{0}\neq0$ (i.e., to find a, non trivial solution), we must I'C(luirc  

$$
\bar{\tt y}\!\cdot\!\bar{\tt y}\,=\,-\beta_{0}^{~2}
$$  

Bccause $\bar{\pmb{\upgamma}}$ may be complcx, Eq. 7..12 is l'c dly t\yO scalar equations. Using Eq. 7.38, \Ye finJ  

$$
(\alpha\cdot\alpha-\beta\cdot\beta)+j2\alpha\cdot\beta=-\beta_{0}^{2}
$$  

or since $\alpha,\,\upbeta.$ , and ${\beta_{0}}^{2}$ are real,  

$$
\begin{array}{c}{{\beta\cdot\beta\,-\,\alpha\cdot\alpha\,=\,{\beta_{0}}^{2}}}\\ {{\alpha\cdot\beta\,=\,0}}\end{array}
$$  

7.2 ,<";.2  PlIA:,\I';  D ";L.\ Y  Axn  .\TTE.'\ UATIOX. \*  To  llnderstand  Eq. $7.4^{\epsilon})$ wc must re(' t!1 that thc "pacc ricpcllllcllC'e of $\mathbf{E}$ and $\mathbf{II}$ is containcd (umpletely in the expollential factor  

$$
e^{-\bar{\Upsilon}\cdot r}=e^{-\alpha\cdot r}e^{-j\beta\cdot r}
$$  

The first factor $e^{-\alpha\cdot r}$ is always real, ,,'!lereas thc second factor $e^{-j{\boldsymbol{\beta}}\cdot\boldsymbol{r}}$ always has unit magnitude.  The phase o f  the second factor varies with  

position as $\upbeta\!\cdot\!r$ .  Therefore a surface of conslant phase is defined by the relation  

$$
\beta{\cdot}r\,=\,\beta r\,\cos\psi\,=\,\mathrm{const}
$$  

with $\beta=\left|\beta\right|$ .   This equation pertains to a plane normal to $\beta,$ as illus­ trated in Fig. $7.3a$ .  

The amplitude of th  field, on the ot her hand, varies as $e^{-\alpha\cdot r}$ .  Ac­ conlingly, a sUI/ocr ( r Cllllstont amplitude is defi necl by the rela tion  

$$
\alpha\cdot r\,=\,\alpha r\,\cos\psi^{\prime}\,=\,\mathrm{const}
$$  

in ,,-h ie!t, by nnalngy ,,-jt h Eq. 7. Li and Fig. $7.3a,\psi^{\prime}$ is the angle between $\pmb{r}$ and $\pmb{\alpha}$ , and $\alpha=\vert\alpha\vert$ .   Again, a plane is dcscribed by Eq. 7.4G.  This plane is norm al (0 $\pmb{\alpha}$ .  

Thc poin t of Eq. 7.-J 3/i is that the rcal vectors $\pmb{\alpha}$ and $\upbeta$ are perpendicu­ lar in  f;pa('C  (if $\alpha,\,\beta\neq0$ ) .  :-' IoreO\'cl·, as long as the frequency is not zero $(\omega\neq0)$ ) , $\beta_{0}>0$ , :lIlcl Eq. $7.43a$ gnanll1tees $\beta\neq0$ .  Specifically  

$$
\beta^{2}\,=\,{\beta_{0}}^{2}\,+\,{\alpha}^{2}\,\ge{\beta_{0}}^{2}\qquad>0\;\mathrm{for}\;\omega\ne\,0
$$  

Therefore, $\dot{\i f}\ \pmb{\alpha}\ \not=\ 0,$ , th e jitfd ( r a nmwmjorm 1Jlane n'ave (Eq. 7.37) has plows of cOilstant allllJlitllrlc (nllrmal 10 $\pmb{\alpha}$ ) and planes of constant phase (llormal to $\upbeta$ ) that o re  III III 1111 IIi! p('rpclUliclilar.  

The moc;t, rapid  c;P:\ ('('-rat e-of-('!tange  of amplitude occurs  in  the dircction of $\pmb{\alpha}$ ( 1.;«_ 7. l (i) ,  \\"!tid\ is perpend i cular to $\upbeta$ and therefore parallel to the plancs of constan t pklf;C.  This field is still a. plane wave, because its equiphase surfaces are planes; but it is not a uniform plane wave, because the field strength varies with position over the equiphase planes.  Similarly, the phase of the field varies most rapidly over the planes of constant amplitude.  

![](images/69bf9661672ade3114e87fbd2962db09dadd27f77d5351d4dc74f8d7a1e3b2ec.jpg)  
F i g .  7.4.  Sign i fi cant. f('a l un's of ( lip SP:lC'C Y:l ri:t1 ion of $e^{-\bar{\mathbf{v}}\cdot\boldsymbol{r}}=e^{-\alpha\cdot\boldsymbol{r}}e^{-\beta\cdot\boldsymbol{r}}$ for non­ uniform plane \\-aYI'S lI"i( hout. l"" ,<,s.  ?\ol e l h:lt ${\mathfrak{a}}{\cdot}{\mathfrak{g}}=0$ , and that t here i  no varia­ l ion at all ill ( he di n'ct ion nnrmal 10 1 11" P:II!;C).  

There is evidently no variation of the field in the direction normal to both $\pmb{\alpha}$ and $\upbeta$ because this direction is characterized by the lines of in­ tersection of planes of constant amplitude with planes of constant phase.  

All the foregoing important features of space variation are illustrated in Fig. 7.4.  

7.2.2.3  TE AND T.i\! PLANE WAVES.\*  We have found that at any nonzero frequency, $\pmb{\alpha}\neq0$ is acceptable to l\1axwell's equations as long as $\upbeta$ obeys Eqs. 7.43.  The somewhat puzzling question of how an "attenuation" can take place in a lossless medium will be answered only after we study the details of the field vectors themselves.  To do this conveniently, choose a $+z$ -axis along $\upbeta$ and a $+y$ -axis along $\pmb{\alpha}$ (always possible,  since $\alpha\cdot\beta=0;$ .  The $+x$ -axis must then be along $\alpha\times\beta$ .  Consequently, as illustrated in Fig. 7.5,  

$$
\bar{\mathbf{v}}\equiv\alpha+j\beta=a_{y}\alpha+a_{z}j\beta\qquad\quad\alpha,\beta>0
$$  

Then Eq. 7.41a becomes  

$$
\alpha\mathrm{E}_{\upsilon0}+j\beta\mathrm{E}_{z0}=0
$$  

Surprisingly enough, Eq. 7.49 docs not restrict $\mathrm{{\bfE}}_{x0}$ in any way.  It is therefore certainly possible to choose as the electric field one with only a single component, in the $x$ -direction, and this electric field automati­ cally satisfies Eq. 7.40.  Such a field is at all times parallel to $\alpha\times\beta$ . It is linearly polarized along the direction in \\'hich there is no space variation of the solution.  One solution of Eq. 7..!0 or Err. $7.\pm1a$ is accordingly  

![](images/e26590d1d8b36aec9a16f726ffefa29afad38db82d6b683637a75683581e0517.jpg)  
Fig. 7.S .  Choice of axes and illustration of field componcnts for $(a)$ TE and (b) Tl\1 planc wavcs in a lo slcss mcdium.  

$$
\mathbf{E}_{0}=\ensuremath{\mathbf{\alpha}}_{\!\!\:x}\mathrm{E}_{x0}
$$  

The magnetic field corresponding to the choice (Eq. 7.50) for the electric field is given by Errs. $7.40a$ and 7.48 :  

$$
\mathbf{II}_{0}=\frac{\bar{\mathbf{\upgamma}}\times\mathbf{\deltaE}_{0}}{j\omega\mu}=\mathbf{\alpha}_{a_{y}}\left(\frac{\beta}{\omega\mu}\right)\mathbf{E}_{x0}-\mathbf{\alpha}_{a_{z}}\left(\frac{\alpha}{j\omega\mu}\right)\mathbf{E}_{x0}
$$  

This magnetic field automatically satisfies Eq. 7.41b, as follows.  

$$
\bar{\mathbf{\Upsilon}}^{\bullet\cdot\mathbf{II}_{0}}=\frac{\bar{\mathbf{\Upsilon}}^{\bullet}(\bar{\mathbf{\Upsilon}}\times\mathbf{\deltaE}_{0})}{j\omega\mu}=\frac{(\bar{\mathbf{\Upsilon}}\times\bar{\mathbf{\Upsilon}}\bar{\mathbf{\Upsilon}})\cdot\mathbf{E}_{0}}{j\omega\mu}\equiv0
$$  

"'e haye in Eqs. 7.50 and 7.5 1 a solution to Eqs. 7.39, because restric­ tions of Errs. 7.4 1 , $7.40a$ , and 7 .·13b arc already met.  Exercise of care to choose $_\alpha$ amI $\beta$ in accordance \yith Eq. $7.43a$ (or Eq. 7.47) \yill then guarantee con;.:istency of Eq. $7.\40b$ .  The magnetic field defined by Eq. 7 . 5 1  is elliptically polarized in the plane $(y,z)$ of $\pmb{\alpha}$ and ${\upbeta}$ , thereby remaining; at all times perpendicular to the eleetrie field descrihed by Eq. 7.50.  Since the electric field has no components in the plane of $\pmb{\alpha}$ and ${\upbeta}$ , in which all space variation takes place, this entire wave solu­ tion may be called a  Tra nsverse mee/rie $(T l)$ piane wave.  The im­ portan t space rein tions nre shown in Fig. $7.\ddot{\circ}a$ .  

$\Lambda$ similar (in fact dual) arp;ument may now be applied, starting from Eq. $7.41b$ instead of Eq. 7.4 1a.  One solution to the former is  

$$
\mathbf{II}_{0}=\ensuremath{\mathbf{a}_{x}}\mathbf{II}_{x0}
$$  

with corresponding electric field given by Eqs. $7.40b$ and 7.48.  

$$
\mathbf{E}_{0}\,=\frac{\mathbf{I}\,\mathbf{I}_{0}\,\mathrm{\boldmath~\times~}\,\bar{\mathbf{\upgamma}}}{j\omega\epsilon}=\,-u_{y}\left(\frac{\beta}{\omega\epsilon}\right)\mathrm{II}_{x0}\,+\,a_{z}\left(\frac{\alpha}{j\omega\epsilon}\right)\mathrm{II}_{x0}
$$  

This electric field automatically satisfies Eq. $7.41a$ .  

Characterized by a map;netic field \\"hich is linearly polarized in the direction of no space Yariation, $\alpha\times\beta$ , and an electric lield elliptically polarized in the plane of $\pmb{\alpha}$ and $\upbeta$ , the solutions in Errs. 7.52 and 7.53 may be ('alled a Transverse J[ aonctie ( TJI) plane \\"aNe.  The relevant illustration is Fig. $7.5\upsilon$ .  

It is cOlwenient to describe the foregoing 'IE nllli T I solutions in a form "'hich does not depend UpOll thc partinilar fat of $(x,\,y,\,z)$ axes chosen in Eqs. 7.48 through 7.33.  As Fig. 7.3 sho\\":: " thc fields can Le described completely by axcs along $\pmb{\alpha},\,\upbeta,$ , awl $\alpha\times\upbeta$ , \\"hich happcn to form a  right-handed rectangul ar  f<ystcm.  ('::;ing unit n;ctors ${\pmb{\alpha}}_{\pmb{\alpha}},\ {\pmb{\alpha}}_{\pmb{\beta}},$ and $\pmb{\alpha}_{\pmb{\alpha}\times\pmb{\beta}}$ along these diredions rcC'pcd i\'ely, amI corrcsponding sub­ scripts $\mathrm{E}_{\alpha},\,\mathrm{II}_{\alpha\times\upbeta}$ , etc., for the field cOlllponcllts, wc may summarize our results in the following way :  

$$
({\bar{\mathfrak{Y}}}={\alpha}+j{\beta};\,{\alpha}\cdot{\beta}=0;\,{\beta}^{2}-\alpha^{2}={\beta_{0}}^{2}=\,\omega^{2}\epsilon\mu)
$$  

$$
{\bf E}={\boldsymbol{a}}_{\alpha\times\upbeta}{\bf E}_{\alpha\times\upbeta,0}e^{-\bar{\upgamma}\cdot r}={\boldsymbol{a}}_{\alpha\times\upbeta}{\bf E}_{\alpha\times\upbeta,0}e^{-\alpha\cdot r}e^{-j\upbeta\cdot r}
$$  

$$
{\bf I I}=\frac{\bar{\bf\Delta}\times{\bf E}}{j\omega\mu}=\left[{\pmb\alpha}_{\alpha}\left(\frac{\beta}{\omega\mu}\right)-\,\llangle{a}_{\beta}\left(\frac{\alpha}{j\omega\mu}\right)\right]\,{\bf E}_{\alpha\times\beta,0}e^{-{\bf\alpha}\cdot{\bf r}}e^{-j{\bf\beta}\cdot{\bf r}}
$$  

$$
{\bf I I}\,=\,a_{\alpha\times\beta}\mathrm{II}_{\alpha\times\beta,0}e^{-\bar{\bf\gamma}\cdot r}\,=\,a_{\alpha\times\beta}\mathrm{II}_{\alpha\times\beta,0}e^{-{\alpha\cdot r}}e^{-j\beta\cdot r}
$$  

$$
{\bf E}=\frac{{\bf I I\,\mu\times\,\bar{\bf\delta}}}{j\omega\epsilon}=\left[{-u_{\alpha}\left({\frac{\beta}{\omega\epsilon}}\right)+u_{\beta}\left({\frac{\alpha}{j\omega\epsilon}}\right)}\right]\mathrm{II}_{\alpha\times\beta,0}e^{-{\alpha\cdot r}}e^{-j{\beta\cdot r}}
$$  

\Ye haye unquestionably ddermined two linearly independent plalle­ waye solutions to Eqs. 7.3D of the form of Eq. 7.37.  1\re there any more solutions of this form?  In \\"hat f'enc-:e there are not may be f'cen by considering an arbitrary linear combination of a 'IE and a 1'.:\1 solution having the same $\bar{\pmb{\upgamma}}$ ,  The combined field meets all the conditions im­ pOf'ed by Eqs. 7,41 and 7.40, pro\'ided that $\bar{\pmb{\upgamma}}$ obeys Eq, 7..J2.  1.10re­ over, Fig. 7.5 shm\'s that the combined field has three f'pace components of both E and II, neither of whic'h i" llecesC'arily lillcarly polarized.  A linear combination oj a TE and a TJ! lJZane 1('0 1'C is thc m ost ucncral sim ple exponential sol ution possiblc Jor a Uivw mIlle oj $\bar{\pmb{\upgamma}}$ consistent 1cith Eq. 7.1/8.  

Ob\·iously, however, e\'en at a  fixed freqnell ey (fixed val ne of $\beta_{0.}$ ) , olle may ehoo:'e mallY differellt "aitH'S of $\bar{\pmb{\upgamma}}$ ('Oll:,;i:,;lL'nt ,,-ith Eqs. 7.·J2 or 7A3.  Fot' example, note ihat eOlldiliolls of Eqs. $7.43a$ (or 7,-l7) and 7.43b allow independent ehoice of the algebraic sign of $\alpha$ and $\beta,$ , given a value of $|\alpha|\propto|\beta|$ anel ginn a freq\lcncy $\omega$ (i,e., givcn a value of $\beta_{0,}$ ). Of course, the relative phases of the field components \rill yary \riih the various possible choices, as shm\'ll by Eqs. 7.31 and 7.33 (ot' 7.5 1 und 7.55).  These faets simply expt'css the idea that, as with unifot'm plane waves, a traveling TE ot' T':\I plane wave oriented in allY direction in space is a \"alid solution of :;\ lax\yeII's cquations as long ns $\mathbf{{F}}_{0},\mathbf{{II}}_{0}$ , and $\bar{\pmb{\upgamma}}$ bear the correct mutual relationships.  X eedless to say, sum::; of TE  and/or 1',:\1 plane ""1\'e::; ill vmious space oricntatioll::; are  abo solutions to thc field cquations,  

7.2.2.4  POWER COXSIDEIUTIOXS AXD \\'AYE bIPEDAXCES.\*  Ex­ amination of thc complcx po\\'er for thc nonuni form planc \\'a\'( s dis­ closcd abovc wil l  hel p to cxplnin the "at tcnuation."  

For cxnmplc, wc hnvc noted that thc cIcetric ficld o f  t hc T E  wa\'c CEq. 7.0-1) is Iincnrly polarizpd in thc direction n ormal t o bol h $\pmb{\alpha}$ nnd ${\mathfrak{G}},$ but thc magnct ic field is ell ipt ically polarized in the plane of $\pmb{\alpha}$ and ${\upbeta}$ . Sincc $\mathrm{F}_{\alpha\times\ B,0}$ an(l $\mathrm{~II}_{\alpha0}$ arc i n  l imc phase, Ihe POm ])Ollcnt of I hn ('oTn !)lp,>, Poynting vcctor along $\upbeta$ i::; entirely 1'l'al.  J IO\\'ever $\mathrm{I}\dot{\cup}_{\alpha\times\beta,0}$ and $\mathrm{~I~I~}_{\beta0}$ arc $90^{\circ}$ out of timc phasc, f:'0  thc componcn t  of the  complcx Poyn ting vcctor along $\pmb{\alpha}$ is  entircly 1'caclil'c.  In  othcr \\'OI'd::; :  only rcal  (timc­ arerage) power flows in the dircction ${\upbeta}$ (norlll al to the com;tant-phase 1Jlanes and  1JCll'Clllcl  to  the  cunsta nt-alll 1Jlitude  J,lancs),  1chl'l'(,((s  only  rcactive powcr flows in the direction $\pmb{\alpha}$ (nol'mal to th e constallt-(!Illl)lilwle 7)la ncs and parallel to the constant-phase ])laIl1'8) .  The "ati elluation" therefore doe::; not act to decrcase with di"taJl('e :Iny "pa('c component of the timc­ U\'crnge pO\\'er and, eOll cqllently, ('all"{'s JlO c1iffic'lI l ty \dl l l  ('oll"crV:I­ t ion of encrgy in the lo" Ie,,s mcd i u m .   Simila r  ('ommcn l s  a pply to thc '1',:\ 1 planc \\'a\'C CEq. 7,;)5) .  Thesc pO\\'cr relat ion h i ps arc i l l ll"tral ed ill Fig. I.ti for bolh ,,·;\\'C types.  

Actually thc idea of a de('rcasinp; field strengl h in a lossle ::; "il uation is qll itc famil iar.  Imagine a ladder net\\'ork of indllctors only, dri\'en from one cnd .  Both the vol tage and the ('\I1'1'('nt "'i l l  dc('r('a e \"ith dis­ tan('c (\\\'ay from the dri\"c terminals ; but f'in('e the "'hole network is reactivc, no real po\\-er entcr::; it from the  O!\\'('e) :lnd no p O\\'cr 10:'::; is impl ied hy the dccreasing vol tage and currcnt leve!:;.  \\'e have simply a lossless "\'oltnge (or clI\'rent) di\'ider. "  

Thc only ncw idea in the llolllllliform plane "-(1\'e field is the pos i­ hility of having rcal unaUcnuatccl POWN flo\\' in onc direct ion, a l lalo­ gous to a travel ing \w\'C on a l assies::; tra nsmission line in t hat d i rect ion, and, at t he snmc time, having a l ossless vol l agc di\'ider ael ion i n  another (pcrpellllicnlar) dircction,  This 1100\'c\'er i::; j u:::t thc kind of dilTcrcn('c \\'e might expect to be brought about by con::;idcring prolllems in more than one spaee dimension.  

Indeed, it is often cOll\'cnicnt to definc in tcrms of field componcnts im pedan('es that deseribe the naturc of the complcx-power components in various spacc directions.  Thus, in gcncral, field components $+\mathrm{l}\mathrm{:}$ a lld $+\mathfrak{l}\mathfrak{l}_{y}$ (or $+\mathrm{I}\!\!\mathrm{;}_{y}$ and $-\mathrm{II}_{x})$ enter into the $+z$ -componcnt of the com plex Poynting vc('tor $\mathrm{S}_{z}$ ) while $+\mathrm{F}_{x}$ and $-\mathrm{II}_{z}$ (or $+\mathrm{l}\dot{z}_{z}$ and $+\mathrm{I}\,\mathrm{I}_{x}$ )  

![](images/b3d299fb57cf972be7b67ed30f44f0b238de9037644c71e6857b4b6fbbe52df1.jpg)  
Fig. 7_6_  Analysis of the complex Poynting vector for nonuniform plane waves in a losslcss mcJium" $(a)$ TE planc wavc ; $(b)$ T:\l plane wavc.   
(b)  

are the pertinent components for $\mathrm{S}_{y}$ The relevant wave impedances may be introduced as foI1O\\-s, using $\mathrm{S}_{z}$ as example :  

$$
\mathrm{S}_{z}=\frac{1}{2}\,\mathrm{E}_{x}\mathrm{H}_{y}{}^{*}-\frac{1}{2}\,\mathrm{E}_{y}\mathrm{H}_{x}{}^{*}=\frac{1}{2}\left(\frac{\mathrm{E}_{x}}{\mathrm{II}_{y}}\right)|\,\mathrm{II}_{y}|^{2}+\frac{1}{2}\left(\frac{-\mathrm{E}_{y}}{\mathrm{II}_{x}}\right)|\mathrm{II}_{x}|^{2}
$$  

Letting  

and  

$$
\begin{array}{l}{{\displaystyle{\bf Z}_{z}^{{\bf\mu}_{2}(x,y)}\equiv\frac{{\bf E}_{x}}{\mathrm{H}_{y}}}}\\ {~~}\\ {{\displaystyle{\bf Z}_{z}^{{\bf\mu}_{2}(y,z)}\equiv{\bf\mu}-\frac{{\bf E}_{y}}{\mathrm{H}_{x}}}}\end{array}
$$  

we have  

$$
\begin{array}{r}{\mathrm{S}_{z}=\,\frac{1}{2}\,\big|\,\mathrm{H}_{y}\big|^{2}\mathrm{Z}_{z}{}^{(x,y)}+\frac{1}{2}\,\big|\,\mathrm{H}_{x}\big|^{2}\mathrm{Z}_{z}{}^{(y,x)}}\end{array}
$$  

Evidently the real and imaginary parts of the wave impedances give the correct algebraic sign of the real and reactive power associated with the pertinent field components.  In many cases, one of the field compOllents responsible for power in a given direetion is absent so that the distinction between the two wave impedanees $[\mathbf{Z}_{z}^{(x,y)}$ and $\mathbf{Z}_{z}^{(y,x)}$ , for example) for that direction need not be made.  In such cases the super­ script will simply be omitted, it being understood from the context which field components must be involved.  

Applying the foregoing ideas to the TE and 1',:\1 plane waves of Eqs. 7.5 ! and 7.53, we may define the following wave impedances :  

$$
\begin{array}{l l}{{\displaystyle{\cal Z}_{\mathfrak{s}}\equiv\frac{{\mathrm{E}_{\alpha\times\mathfrak{s},0}}}{\mathrm{H}_{\alpha0}}=\frac{\omega\mu}{\beta}}}&{{\qquad\mathrm{(c)}\quad{\cal Z}_{\mathfrak{s}}\equiv\frac{-\mathrm{E}_{\alpha0}}{\mathrm{H}_{\alpha\times\mathfrak{s},0}}=\frac{\beta}{\omega\epsilon}}}\\ {{\displaystyle{\cal Z}_{\alpha}\equiv\frac{{\mathrm{E}_{\alpha\times\mathfrak{s},0}}}{-\mathrm{H}_{\mathfrak{s}0}}=\frac{\dot{j}\omega\mu}{\alpha}}}&{{\qquad\mathrm{(d)}\quad{\cal Z}_{\alpha}\equiv\frac{\mathrm{E}_{\beta0}}{\mathrm{H}_{\alpha\times\mathfrak{s},0}}=\frac{\alpha}{\dot{j}\omega\epsilon}}}\end{array}
$$  

Observe that, if $\beta>0,\mathrm{~Z_{\ttB}~}$ is positive real, indicating again that only time-average power flows in the $\upbeta$ direction.  If $\alpha>0$ , $\mathbf{Z}_{\alpha}$ is inductive for the TE wave, indicating that reactive power only flows in the $\pmb{\alpha}$ direction and that the 'TE field stores mOTe time-average magnetic than electric energy pCI' unit volume.  On the other hand, $\mathrm{\bfZ}_{\alpha}$ is capacitive for the Tl'.l w::we, which means that the 'Til! field stores mOTe time-average electric than magnetic energy per unit volume.  These facts are also in­ eluded in Fig. 7.0.  

The most general losslcss plane ,mve with a given $\bar{\pmb{\upgamma}}$ is, as we have already mentioned, a liuear combination of a TE and a Tl'.1 plane wave with respect to the direction of the vectors $\upbeta$ amI $\pmb{\alpha}$ .  It is not difIicult to see in Fig. 7.5 that the field components missing from these u'aves make them orthogonal with respect to complex power in the ${\upbeta}$ and $\pmb{\alpha}$ directions. That is, the complex power in these directions ,,"hell both waves are present together is the sum of the complex powers which would be carried in these directions by each one separately. Unfortunately, how­ ever, this orthogonality docs not hold for complex power in the direc­ tion normal to $\pmb{\alpha}$ and $\upbeta$ (i.e., the direction of $\alpha\times\upbeta.$ ) .  For either wave alone ${\mathrm{\bfS}}_{\alpha\times\beta}\equiv0_{:}$ , but, when both are present together, Eqs. 7.54 and 7.53 show that  

$$
\mathrm{S}_{\alpha\times\mathfrak{b}}=\frac{1}{2}\left(\mathrm{E}_{\alpha}\mathrm{I}\mathrm{I}_{\mathfrak{b}}{}^{*}-\mathrm{E}_{\mathfrak{b}}\mathrm{I}\mathrm{I}_{\alpha}{}^{*}\right)\,=\frac{j\alpha\beta}{\beta_{0}^{2}}\,\mathrm{I}_{\alpha\times\mathfrak{b},0}\,\mathrm{E}_{\alpha\times\mathfrak{b},0}e^{-2\alpha\cdot r}
$$  

This is not in general zero, but depends upon $\mathrm{E}_{\alpha\times\beta,0}$ and $\mathrm{II}_{\alpha\times\beta,0;}$ , which '\'e have seen are independent as far as l\Iaxwell's equations are con­ cerned.  Their presence and rel::ttive magnitude and phase will there­ fore be determined completely by boundary conditions.  

# 7.2.3 Relationships  b etween  Uniform and Nonuniform Plane Waves \*  

Thc r(' mlis of our \york in Secs. 7.2 . 1  amI 7.2.2 may bc i:>ummarizcd us follO\ys : The field  

$$
{\bf E}={\bf E}_{0}e^{-\bar{\bf\Delta}\cdot r}={\bf E}_{0}e^{-\bar{\bf\Delta}\cdot r x}e^{-\hat{\tau}_{y}y}e^{-\bar{\tau}_{z}z}
$$  

$$
\mathbf{II}=\mathbf{II}_{0}e^{-\frac{\mathbf{\nabla}\cdot\mathbf{\nabla}r}{\mathbf{\nabla}\cdot\mathbf{\xi}}}=\frac{\breve{\mathbf{\nabla}}\times\mathbf{\nabla}\mathbf{E}_{0}}{j\omega\mu}\,e^{-\bar{\mathbf{\xi}}\cdot\mathbf{\nabla}r}=\frac{\breve{\mathbf{\nabla}}\times\mathbf{\nabla}\mathbf{E}}{j\omega\mu}
$$  

is a sinusoidal steady-statc solution to l\1uxwcll's equations without loss if and only if thc conditions  

$$
\bar{\gamma}_{x}{}^{2}+\bar{\gamma}_{y}{}^{2}+\bar{\gamma}_{z}{}^{2}=\,-\beta_{0}{}^{2}(\,=\,-\omega^{2}\epsilon\mu)
$$  

and  

$$
\left\{\begin{array}{l l}{{\displaystyle\bar{\gamma}_{x}\mathrm{E}_{x0}+\bar{\gamma}_{y}\mathrm{E}_{y0}+\bar{\gamma}_{z}\mathrm{E}_{z0}=0}}\\ {{\displaystyle\bar{\gamma}_{x}\mathrm{I}\,\mathrm{I}_{x0}+\bar{\gamma}_{y}\mathrm{I}\,\mathrm{I}_{y0}+\bar{\gamma}_{z}\mathrm{I}\,\mathrm{I}_{z0}=0}}\end{array}\right.
$$  

arc satisfie(l.  Xotc that :1I1y bn) of $\overline{{\gamma}}_{x},\,\overline{{\gamma}}_{y},\,\overline{{\gamma}}_{z}$ arc complctely arhitra ry ('omplex numbers, \yitlt the third fi xed (ex{'cpt for al cbraic sign) by Eq. $7.5\!\cdot\!9\!(t$ .  Simila rly, any two of $\mathrm{I}\mathrm{:}_{x()},\,\mathrm{I}\mathrm{:}_{\iota_{;\prime}()},\,\mathrm{I}\mathrm{:}_{z()}$ (or $\mathrm{I}\,\mathrm{I}_{x()},\,\mathrm{I}\,\mathrm{I}_{y()},\,\mathrm{I}\,\mathrm{I}_{z()}\big)$ arc abo com pldely a rbi t ra ry c OJllplex l luml wrs,  with the third fixed by Eq.  7.;J!)1i.  Equat ion 7.581i thell determilles the remaining complex yector $\mathbf{I}\mathbf{I}_{0}$ (or $\mathbf{I}\dot{\boldsymbol{\lambda}}_{0}^{\mathrm{~\,~}}$ ) .  

The fol lowing special ca"es haye arise1l :  

1 .  If ${\bar{\tt Y}}=j{\tt B}$ (i.e., ${\pmb{\alpha}}=0]$ ) ,  the solution is a  uniform  plane wave, whit-It is olle form of the TK\ 1 \\"a\'e with rcsped to ${\upbeta}$ .  

2.  If $\pmb{\alpha}\neq0$ and $\mathbf{{I}}\dot{\ensuremath{\mathbf{{z}}}}_{0}=\ensuremath{\lambda}\mathbf{{\bar{}}}E_{0},$ , ,,-hcre $\Lambda$ i:; allY complex lluml)er and $\pmb{{\cal E}}_{0}$ any real H'ctor ,  the solut ion has a linearly polarized electric field and is a TE \\"aye \"ith re"pcet to $\upbeta$ atHl $\pmb{\alpha}$ .  

3 .   If $\pmb{\alpha}\neq0$ a l l< l $\mathbf{II}_{0}\,=\,\mathrm{I};I\pmb{I}_{0},$ , \\"h('rc $1\}$ is allY complex Ilumher alld $\pmb{I}_{\cup}$ allY rcal  \'edor,  t he sol u t ion has a  linearly polarized magnetic  field and is a T'\ l mln  with rC"Jlc('t to ${\upbeta}$ and $\pmb{\alpha}$ .  

4.  ]f $\pmb{\alpha}=0$ , togdhcr \\"ith cither $\mathbf{{I}}\dot{\ensuremath{\Sigma_{0}}}=\ensuremath{\lambda}\mathbf{{\bar{\rho}}}\ensuremath{\lambda}\ensuremath{\lambda}\ensuremath{\lambda}\ensuremath{\lambda}_{0}$ or $\mathbf{II}_{0}\,=\,\mathrm{I}3\pmb{I}\pmb{I}_{0},$ thcn the "ol ut ion is a  uniform plane ml \'e \\"ith linearly polarized electric alld magllctic fields.  

"'e i'ee from thc summary that the condition of Eq. $7.59a$ is of great importance.  It w a s  met automatically ill the ease of the uniform plane \nt\"e $(\pmb{\alpha}=0)$ by the "'cIl-kIlO\\'ll  eometric condition  ( Eq. 7 . 1 7)  on the direction co ines $(l_{z},\,\eta\iota_{z},\,n_{z^{\prime}})$ of the propagation direction with re pect to the $(x,\,y,\,z)$ axes.  What, if any, are the j2;eometric c on!:'e­ quellces of Eq. $7.59a$ "hen $\pmb{\alpha}\neq0$ ·?  

![](images/57bb61703384479905099031ea3dd347c10187cd612a1515de246f3b5d68c185.jpg)  
F i g. 7.7.  Polar angles for location of a new axis.  

With reference t o  Fig. 7.7, let $+z^{\prime}$ b e  n n  nxis nlong $\upbeta$ for fl, ?IIufonn plane waye.  In;;t ead of loC'ating $+z^{\prime}$ hy its direction C'o:-ine;;, usc the polar nngles $\vartheta$ amI $\varphi$ shO\m.  Theil the direction c.:o"jnes of $+z^{\prime}$ nrc :  

$$
\begin{array}{r l}&{\ l_{z^{\prime}}=\sin\vartheta\,\cos\varphi}\\ &{m_{z^{\prime}}=\sin\vartheta\,\sin\varphi\,\Biggr\}\,0\leq\vartheta\leq\pi\qquad0\leq\varphi<2\pi}\\ &{n_{z^{\prime}}=\cos\vartheta}\end{array}
$$  

It is obviolls t hnt ${l_{z^{\prime}}}^{2}+{m_{z^{\prime}}}^{2}+{n_{z^{\prime}}}^{2}\equiv1$ nutomnti('nlly w]H'n rx))re;;,,('(l thus in terms of $\vartheta$ nnd $\varphi$ P.  

The exponent ial f:lctor in the fields therefore becomes  

$$
e^{-{\bar{\bf\Delta}}\cdot r}\,=\,e^{-j{\bar{\bf\Delta}}\cdot r}\,=\,e^{-\,(j\beta_{0}\sin\vartheta\cos\varphi)x-(j\beta_{0}\sin\vartheta\,\sin\varphi)y-(j\beta_{0}\cos\vartheta)z}
$$  

so that we may write  

$$
\begin{array}{l}{{\bar{\gamma}_{x}=j\beta_{0}\,\sin\,\vartheta\,\cos\,\varphi}}\\ {{\bar{\gamma}_{y}=j\beta_{0}\,\sin\,\vartheta\,\sin\,\varphi}}\\ {{\bar{\gamma}_{z}=j\beta_{0}\,\cos\,\vartheta}}\end{array}
$$  

with the consequence that, iclenticnlly,  

$$
\overline{{\gamma}}{_x}^{2}+\overline{{\gamma}}{_y}^{2}+\overline{{\gamma}}{_z}^{2}\equiv-{\beta_{0}}^{2}
$$  

# 332  ElECTROMAGNETIC ENERGY TRANSMISSION AND RADIATION  

The important point now is the fact that  

$$
\sin^{2}{\bar{\vartheta}}\,\cos^{2}{\bar{\varphi}}+\sin^{2}{\bar{\vartheta}}\,\sin^{2}{\bar{\varphi}}+\cos^{2}{\bar{\vartheta}}\equiv1
$$  

when $\overrightarrow{\vartheta}$ and $\bar{\varphi}$ are any arbitrary complex numbers!  

In other words, if we allow the notion of complex polar angles $\bar{\vartheta}$ and $\bar{\varphi}$ for the direction of propagation of a uniform plane wave, the cor­ responding solution becomes a nonuniform plane wave with complex $\overline{{\gamma}}_{x},\overline{{\gamma}}_{y},\overline{{\gamma}}_{z}$ defined by Eq. 7.62 and satisfying the condition of Eq. $7.59a$ identically.  

An illustrative example of the complex angles is furnished by the case treated in Sec. 7.2.2.3, where  

$$
\begin{array}{r}{\tilde{\mathbf{y}}=\mathbf{\boldsymbol{a}}_{y}\alpha+\mathbf{\boldsymbol{a}}_{z}\j\beta\qquad(\mathbf{\boldsymbol{\alpha}},\beta>0)}\end{array}
$$  

and  

$$
\beta^{2}=\beta_{0}^{~2}+\alpha^{2}>\beta_{0}^{~2}
$$  

In this case it is easiest to start with Eq. $\mathbf{7.62}a$ because $\bar{\gamma}_{x}=0$ .  In other cases, Eq. $\mathbf{7.62c}$ might be simpler because it contains only one angle.  

Thus in the present example  

$$
\bar{\gamma}_{x}=0=\sin\bar{\vartheta}\cos\bar{\varphi}
$$  

so either sin $\bar{\vartheta}\,=\,0$ or $\cos\bar{\varphi}=0,$ , or both.  But ${\bar{\gamma}}_{y}\neq0.$ , so Eq. $7.62\boldsymbol{b}$ shows that sin $\bar{\vartheta}\neq0$ .  lIence we must choose cos $\bar{\varphi}=0$ .  Since, how­ ever $\bar{\varphi}$ is a complex angle $\varphi_{\mathit{R}}+j\varphi_{I},$ we must set  

$$
\cos\bar{\varphi}=\,\cos\left(\varphi_{R}+j\varphi_{I}\right)\,=\,\cos\varphi_{R}\cosh\varphi_{I}-j\sin\varphi_{R}\sinh\varphi_{I}\,=\,0
$$  

Because cosh $\varphi_{I}\geq1,$ this implies in sequence  

$$
\begin{array}{c c}{{\displaystyle{\varphi_{R}=\frac{\pi}{2}\bigg(\mathrm{or\,}\frac{3\pi}{2}\bigg)}}}&{{0\leq\varphi_{R}<2\pi}}\\ {{\mathrm{}}}&{{\mathrm{}}}\\ {{\sin\varphi_{R}=+1\,\mathrm{(or-1)}}}&{{}}\\ {{\mathrm{}}}&{{\mathrm{}}}\\ {{\varphi_{I}=0}}&{{}}\\ {{\mathrm{}}}&{{\mathrm{}}}\\ {{\sin\bar{\varphi}=\sin\varphi_{R}=+1\,\mathrm{(or-1)}}}\end{array}
$$  

Now with reference to $\bar{\gamma}_{y}$ in Eq. 7.62b, we need to know that  

$$
\sin\bar{\vartheta}\,=\,\sin\,(\vartheta_{R}+j\vartheta_{I})\,=\,\sin\vartheta_{R}\,\cosh\vartheta_{I}+j\cos\vartheta_{R}\,\sinh\vartheta_{I}
$$  

It follows from this result, with the usc of Errs. 7.48, $7.62\boldsymbol{b}$ , and the con­ dition of Eq. $7.64d$ on sin $\bar{\varphi}$ , that  

$$
\alpha=\,_{(-)}^{+}\beta_{0}(j\sin\vartheta_{R}\cosh\vartheta_{I}-\cos\vartheta_{R}\sinh\vartheta_{I})
$$  

Therefore, since $_{\alpha}$ is positive real and cosh $\vartheta_{I}\geq1,$ we have in sequence that  

$$
\sin\vartheta_{R}\cosh\vartheta_{I}=0
$$  

$$
\vartheta_{R}=0\,\left[\mathrm{or}\;\pi\right]\qquad0\leq\vartheta_{R}<2\pi
$$  

$$
\cos\vartheta_{R}=1\;[\mathrm{or}-1]
$$  

$$
\alpha=\,_{(-)}^{+}\beta_{0}\bigl(_{[+]}^{-}\sinh\vartheta_{I}\bigr)>0
$$  

where we have used the curved $(-)$ and square $[+]$ marks in Eq. 7.G5d to identify the algebraic sign alternatives from Eqs. $7.64d$ and $7.65c$ respecti vely.  

To eliminate some of the various choices of algebraic sign  and quadrant of angle remaining, we must look at Eq. $\mathbf{7.62c}$ , when $\bar{\gamma}_{z}=j\beta_{s}$ , as required by Eq . 7.48.  We find  

$$
\beta\,=\,\beta_{0}(\cos\vartheta_{R}\cosh\vartheta_{I}-j\sin\vartheta_{R}\sinh\vartheta_{I})\,=\,\beta_{0}\cos\vartheta_{R}\cosh\vartheta_{I}>0
$$  

in view of Eq. 7.G5b.  

Again, since cosh $\vartheta_{I}\geq1,$ cos $\vartheta_{R}>0$ .  This means  

$$
\vartheta_{R}\,=\,0\,\left(\mathrm{not}\:\pi\right)
$$  

in Eq. 7.G5b, which removes completely the [ ] alternatives in Eqs. $7.65d$ .  Accordingly, using the first choice in Eq. 7.G5c, we have  

$$
\cosh\vartheta_{I}=\frac{\beta}{\beta_{0}}>1
$$  

which leaves the algebraic sign of $\vartheta_{I}$ still in doubt.  

We are left with a choice of two solutions.  Either  

$$
\varphi_{R}=\frac{\pi}{2}
$$  

and  

$$
\sinh\vartheta_{I}\,=\,-\,\frac{\alpha}{\beta_{0}}
$$  

or  

$$
\varphi_{\!R}=\frac{3\pi}{2}
$$  

and  

$$
\sinh\vartheta_{I}=+\frac{\alpha}{\beta_{0}}
$$  

The existence of these two possibilities has no particular physical significance.  They are simply consequences of the multiple-valued  

# 334  ELECTROMAGNETIC  ENERGY TRANSMISSIO N  AND RADIATIO N  

properties of the inverse trigonometric functions.  A uniform plane wave at either set of complex angles  

and  

or  

$$
\begin{array}{l}{{\bar{\vartheta}\,=\,-j\sinh^{-1}\left(\displaystyle\frac{\alpha}{\beta_{0}}\right)}}\\ {{\,}}\\ {{\bar{\varphi}\,=\,\displaystyle\frac{\pi}{2}}}\\ {{\,}}\\ {{\bar{\vartheta}\,=\,+j\sinh^{-1}\left(\displaystyle\frac{\alpha}{\beta_{0}}\right)}}\\ {{\,}}\\ {{\bar{\varphi}\,=\,\displaystyle\frac{3\pi}{2}}}\end{array}
$$  

and  

repre::-ents physical ly the sall l c  nOlwll1jonn plane ,,'ave.  "Te can choose either solution arbi t ra rily.  Xcedlc s  to  ::-ay, the polarization of the uniform plane \\,ave  ets the TE, 1',:\ 1, or combined TE-T':\I character of the result ing \\'a ve.  

Om understandillg of the pl:me-wa \'e solut ions we have foun(l will be weak unless \\'e apply them t o   Oll1e f:'ituations invol ving boulllbries. The principal pl\l'po e of the follo"'ing Hections of this chapter is there­ fore t o  discuss Home problems in \"hich it only takes a small number­ one, t\\'O, three, etc.-of plane ,,'a yes to meet the bounda ry conditions. '" e shall find many m:eful similarit ies bet"'ecn t hese problems alltl those encountered in tranf:'mis::-ion lines, but there are abo important dif­ ferences.  The differences arise from both the three-dimensional varia­ tion of the fields, and their three-dimensional vector character.  The examples cho en do illustrate significant physical phenomena in optics and radio transmission, but they arc equally important as part of a background of  understood  eases upon which  to develop  a physical intuition suitable for dealing with harder field problems.  

# 7.3  Normal Incidence of a Uniform Plane Wave  

'Ve suggested in connection with Eqs. 7 .14 and 7.15, that \\'e could interpret the $(+)$ solution for a uniform plane wa\'e as an incident \\'ave and the $(-)$ one as a reflected \\'ave.  We abo suggest ed ill Sec. 7. 1 .5, hO\\,ever, that sueh an interpretation ,,'oull! be meaningful only if the boundary eonditions in all spacc could be met by Eq. 7.14.  Specifically, we must have a physical situation in three-dimensional space for whieh the boundary conditions require only $x$ -polarized uniform plane waves propagating in the $\pm z$ directions.  

1\ o w  the bound ary conditions for the complex fields involve only componcnts  of $\mathbf{\boldsymbol{\mathrm{F}}}$ and  II  tangcntial  to intcrfaccs  bct\\'een diffcrcnt mcdia (Eqs. 1.2  and 1 .2;") .  If we take the incident \\'twe (specified by some rcmote sOll]"('e) as an $\mathscr{X}$ -polarizc(l uniform planc wavc propagnt­ illg in the $+z$ dircction, its e1cctric and magnctic fields lie in planes normal to the $z_{\mathrm{-}}$ -axis and extcwl uniformly throughout these planes. Thus a pianc boundary or intcrfacc bet wecn differcnt media which abo extends uniformly in  omc piane normal to the z-axis should require ollly similar field compollcnts in the rcflcc tcd wavc.  

# 7.3 . 1   Normal Incidence o n  a Perfect Conductor  

For a fir t examplc, considcr thc situation in Fig. 7.8.  A pcrfectly conducting mctal wall occupics the cntire $x,\,y$ plane, and the incidcnt  

![](images/e5950c1fd2ca1c277ab39269a3e5f7c272acd1055484629feda77851f5c61eab.jpg)  
F i g .  7.8.  Kurmal incidence uf uniform plane  wave  all  a  perfect  cunductor. The $+y$ -axis points out of the paper.  

uniform plane wave (from a source at $z=-\infty$ ) has the specificd form  

$$
\mathbf{E}_{i}=\,a_{x}\mathrm{E}_{x0}{}^{+}e^{-j\beta_{0}z}
$$  

in which ${\mathrm{F}_{x0}}^{+}$ is $^\mathrm{a}$ givcn constant.  In accordance with Eqs. 7. 14, thc COlTc;;pomling magnctic field is  

$$
{\bf{I I}}_{i}=\displaystyle{{\bf{u}}_{y}\frac{\mathrm{{E}}_{x0}{}^{+}}{\eta}}\,e^{-j\beta_{0}z}
$$  

allu the reIlectcu field will oe ucnotcu by  

$$
\begin{array}{l}{\displaystyle\mathbf{E}_{r}\,=\,a_{x}\mathrm{E}_{x0}-e^{j\beta_{0}z}}\\ {\displaystyle\mathbf{II}_{r}\,=\,-\,a_{y}\,\frac{\mathrm{E}_{x0}-}{\eta}\,e^{j\beta_{0}z}}\end{array}
$$  

The boundary condition on thc mctal wall requircs the t0tal tan­ gential electric field to vanish whcn $z=0$ for all $\pmb{x}$ and $\emph{y}$ .  Therefore  

$$
\mathrm{E}_{x0}{}^{+}+\mathrm{E}_{x0}{}^{-}=0
$$  

![](images/fe4fcf88ca61bc404de41423883b3ee13d3d8c1355bc4dc50f6c26be893472cd.jpg)  
Fig. 7.9.  Lossless transmission line analog for Fig. 7.8 with $_x$ -polarized uniform plane \Va ves.  

and the total field becomes  

$$
\mathbf{E}=\mathbf{E}_{i}+\mathbf{E}_{r}=\,-a_{x}2j\mathrm{E}_{x0}^{}+\sin\beta_{0}z
$$  

$$
\mathbf{II}\,=\,\mathbf{II}_{i}+\mathbf{II}_{r}\,=\,a_{y}\,\frac{2\mathrm{E}_{x0}{}^{+}}{\eta}\cos\beta_{0}z
$$  

We see that, hCf'ides being perpendicular in space, $E\,[=\,\mathrm{Re}\,\left(\mathrm{E}e^{j\omega t}\right)]$ and ${\cal U}\left[=\mathrm{Re}\left(\mathbf{II}e^{j\omega t}\right)\right]$ a r c $90^{\circ}$ out of phase \yith ref'pect to both their time and space yariations.  Indced, E and II havc relative phases and space variations exactly like the voltage and current respectively on a short-circuited 10f'sless transmission line.  As a matter of fact, if we simply remember that $\mathbf{\deltaF}$ lies along the $x$ -axis amI. II lies along the $\mathcal{Y}$ -axis, the solution (Eq. 7.70) is otherwise identical with that of the trans­ missioll line in Fig. 7.9.  Note that the "characteristic wave impedance"  

![](images/ab3fa04ba78a72b3ad2ae69c884757275a02bf39779da3938afdbcd3850e0d37.jpg)  
Fig. 7 . 1  o.  St Ulding-\\"ave pattei'll in fronL of a pPI"fect conductor illuminuted by a normally incident, $+x$ -polarized ulliform pi aIle wave.  

$\pmb{\eta}$ serves as characteristic impedance of the line in this case.  In Fig. 7. 10 ,,"e sho\\' space plots of $\pmb{{\cal E}}$ and $\pmb{U}$ at a moment \yhen neither one has its maximum magnitude.  The relation bet,,"een this figure and Fig. 3.0 should be studied carefully.  

A little thought will convince us that, had \ye started with a y­ polarized incident wave, the reflected wave ,,"ould also have been $\mathcal{Y}$ -polarized, and the standing-\\"ave pattern of Fig. 7.10 would merely have been rotated about the $+z$ -axis clockwise by $90^{\circ}$ in space.  ::'.lore­ over, the equivalent transmission line of Fig. 7.0 would have remained the same, except that $\mathrm{E}_{y}$ woukl have replaced $\mathrm{F}_{x}$ , and $-\mathrm{II}_{x}$ would have replaced $\mathrm{II}_{y}$ (see Eqs. 7.2 and compare Eqs. 7.3 and 7.8).  

If the incident uniform plane wave had electric field components along both the $\boldsymbol{x}$ and the $\mathcal{Y}$ directions, \ye would simply treat each component (with its associated magnetic field according to Eqs. $7.5a$ and $7.9a\!\!\!/$ ) separately, amI superpose the separate solutions after com­ pleting them independently.  

# 7.3.2  Normal Incidence on a Lossless Dielectric  

Our second exampIc of a plane boundary normal to the direction of propagation of the incident mwe involves two lossless dielectrics, as appear in Fig. 7. 1 1 .   The incident wave is given i n  medium 1 as an $_x$ -polarized uniform plane \\"ave :  

$$
\mathbf{E}_{i}=a_{x}\mathrm{E}_{x1}{}^{+}e^{-j\beta_{01}z}
$$  

$$
\mathbf{II}_{i}=\frac{1}{\eta_{1}}\,\mathbf{\boldsymbol{a}}_{z}\,\times\,\mathbf{E}_{i}
$$  

'Ye must, in this case, allo\\' for a wave transmitted into medium 2 as ,yell as for a reflected wave ill medium 1.  "-e shall as:-mme, how­ ever, that no $(-)$ W l\'e occurs in medium 2.  Some discussion is ill order to indicate that the absen('e of a $(-)$ \\"ave is ill fact an assump­ tion.  There is a temptation to try to  ummarize it simply by pointing out that medium 2 extends illfinitely far to the right, and by sugge:-;ting that no wave has time to come back from slIch a distance.  These statements, hO\\"e"er, do not explain the absence of a $(-)$ W l\"e in $^{a}$ lossless medium in Ihe sin usoidal steady state.  The steady-state idea itself supposes that \ye have, in fact, waited long enough for all initial transients to disappear, eycn if t.hat takes infinite time !  For example, if there were a perfectly conducting plane at $z=z_{0}>0$ , our previous ,,"ork shows that there would certainly be a $(-)$ wave in medium 2, no matter how large $z_{0}$ might be.  If there is to be no $(-)$ wave, the important point is not how far medium 2 extends but rather that there cannot be (for example) :1 metnl plane at the end of it, eycn if the end is at $z=+\infty$ .  The hOl1Pf't way to sta t e  our prcscnt a,,:,;umption is $a s~a$ boundary condition on the solution when $z\rightarrow+\infty$ .  Spccifically, "'e are arbitrarily  looking  for  a  sol u t i on  \yhi (:h  behaves  l ike  :1  right-goi ng \yave $e^{-j\beta_{02}z}$ as $z\rightarrow+\infty$ .  

![](images/1c705132a814dba421a9013886d20cde768fe8437132226ac8d7c11dd7043887.jpg)  
F i g .  7.1 1 .   Normal incidence of uniform plane wave on a lossless dielectric.  

The immediate question is then \d lCther such :1 f'olution can be found. If it c a n ,  the ensuing que:,;tioll of what rml physic-a I situations m ight correspond to it is quite another matter.  Dealing wit h this one reqllires physical j udgcments, the successful  making of ,yliich ilwol ycs more than ,ye can profitably discuss at this point in our argument.  

Heturning, then, to the solution itself, we takc thc form of thc rc­ flected wavc in mcdium 1 to be  

$$
\begin{array}{l}{\displaystyle\mathbf{E}_{r}=\,a_{x}\mathrm{E}_{x1}^{\phantom{\dagger}}\mathbf{-}e^{j\beta_{01}z}}\\ {\displaystyle\mathbf{II}_{r}=\,-\,\frac{1}{\eta_{1}}\,a_{z}\,\mathrm{\boldmath~\times~}\,\mathbf{E}_{\tau}}\end{array}
$$  

and thc form o f  thc transmittcd wave in mcdium 2 to bc  

$$
\begin{array}{l}{{\bf{E}}_{t}={a_{x}}{\mathrm{{E}}_{x2}}^{+}{e^{-j{\beta_{02}}z}}}\\ {\mathrm{{\bf{II}}}_{t}=\frac{1}{{\eta_{2}}}{a_{z}}\,\mathrm{\times}\,{\mathrm{{E}}_{t}}}\end{array}
$$  

The boundary conditions at thc intcrface $z=0$ rcquirc both $\mathbf{E}_{\mathtt{t},\mathtt{n}\mathtt{s}}$ and $\mathbf{II}_{\mathtt{t a n g}}$ to bc continuous:  

$$
\begin{array}{r l r}{\mathbf{E}_{i}+\mathbf{E}_{r}=\mathbf{E}_{t}\quad}&{{}}&{\mathrm{at}\;z=0}\\ {\mathbf{II}_{i}+\mathbf{II}_{r}=\mathbf{II}_{t}\quad}&{{}}&{\mathrm{at}\;z=0}\end{array}
$$  

Using Eqs. 7.71, 7.72, amI 7.73 in Eq. 7.74, w e  have  

$$
\mathrm{E}_{x1}{}^{+}+\mathrm{E}_{x1}{}^{-}=\mathrm{E}_{x2}{}^{+}
$$  

$$
\frac{1}{\eta_{1}}\,({\mathrm{E}_{x1}}^{+}-\,{\mathrm{E}_{x1}}^{-})\,=\frac{1}{\eta_{2}}\,{\mathrm{E}_{x2}}^{+}
$$  

l\ Iultiplication  of  Eq. $7.75\upsilon$ by $\eta_{2}$ ,  and subtraction from Eq. $7.75a$ yields  

$$
\frac{\mathrm{E}_{x1}^{\phantom{+}}-}{\mathrm{E}_{x1}^{\phantom{+}}+}\equiv\bar{\mathrm{I}}_{\mathit{R}}=\frac{(\eta_{2}/\eta_{1})\,-\,1}{(\eta_{2}/\eta_{1})\,+\,1}
$$  

which, i n  turn, upon substitution back into Eq. $7.75a$ also gives  

$$
\frac{\mathrm{j.}_{\mathrm{r2}}^{\mathrm{~\,~+~}}}{\mathrm{j.}_{\mathrm{r1}}^{\mathrm{~\,~+~}}}\equiv\mathrm{\bf~\hat{I}^{\mathrm{~\,~}}}=\frac{2(\eta_{2}/\eta_{1})}{(\eta_{2}/\eta_{1})+1}
$$  

The usc of the symbol $\bar{\Gamma}_{R}$ in Eq. $7.76a$ stems from its dear analogy \\"itl! t he reflection coefficient of the load on a transmission line.  In this cuse, the reflect ion cl)('./ficiml $\bar{\Gamma}_{\mathit{l}\mathit{i}}$ is lhc ratio at lhc interJace oj lhe colI/plc.r nj{ecled electric field to the cOlllple,C incidcnl electric field.  Indeed, both Eqs. 7.7(ia a l ld 7.7(ib (or 1<:< /:-;. 7.75) follow from the equivalent tra n;;m ission-linc system,  lOh O\\" J \  i n  Fig.  7. 1 2,  in \\"hich  the incident "vol tage" ${\mathrm{l}}{\mathrm{}}\mathrm{}_{\varepsilon1}{}^{+}$ is regarded a s  given.  \\'e can lOee this dearly by first rcp\a('ing the l'c('olHl transmis"ion line in Fig. 7. 12 according to the modified form of Thc\'cnin's theorem proved for the time domain in Chapter ·J.  This step yiellls Fig. 7. 13, from which Eq. $7.76a$ becomes apparent.  

?\ext, \\'e also repiaee line 1 in Fig. 7. 13 by its TMvcnin equivalent on the l'ame basis, remembering that $\mathrm{l}\mathrm{:}_{x1}{}^{+}$ (the inei(lent wave) is given. There results Fig. 7 . 1 ·1, exhibiting dearly Eq. $7.76l)$ .  The symbol T in  this equation is called  the  tran::;lIli::;siun cuefficient, defined as  the ratio at the interface of the complex transmitted electric field to the complex incident electric field.  

![](images/6adedd65b2c49c1338e597f710c8c899c0851663ef3da0482fe2d7879f9abc51.jpg)  
F i g .   7.1 2.  Lossless  transmission  line analogy for Fig. 7.1 1 .  

![](images/a6af7872ea10ae96e0cc71fe12259c8f06b16039fb497b7f2e434f141f71b008.jpg)  
Fig. 7.1 3.  An equivalent  circuit for  Fig.  7. 12 from the point of view of line  1.  

![](images/452fe95bc1672565160a5975aa519681913be26cfecc39c30bd61be62cd91f5a.jpg)  
F i g .  7.1 4.  Complete equivalent circuit of Fig. 7.12 at $\boldsymbol z=0$ .  

It follows from Eqs. $7.75a$ , and the definitions of $\bar{\Gamma}_{R}$ and $\mathbf{T}$ in Eqs. $7.76a$ and 7.7Gb, that  

$$
1+\bar{\Gamma}_{\!\ensuremath{\mathbb{R}}}=\ensuremath{\mathbb{T}}
$$  

Also we note that the time-average power per unit area carried in the $+z$ direction in medium 1 is  

$$
\left\langle S_{z1}\right\rangle=\frac{|\,{\mathrm{E}}_{x1}^{\quad+}|^{2}-|\,{\mathrm{E}}_{x1}^{\quad-}|^{2}}{2\eta_{1}}=\frac{|\,{\mathrm{E}}_{x1}^{\quad+}|^{2}}{2}\,\eta_{1}(1-|\,\bar{\Gamma}_{R}|^{2})
$$  

and that carried in the $+z$ direction in medium 2 is  

$$
\langle S_{z2}\rangle=\frac{|\mathrm{E}_{x2}+|^{2}}{2\eta_{2}}
$$  

Since the interface is lossless, these should be equal  

$$
\left(\!\frac{\eta_{1}}{\eta_{2}}\!\right)\!|\mathrm{T}|^{2}=1-|\,\bar{\Gamma}_{\!R}|^{2}
$$  

and direct substitution of Eqs. $7.76a$ and $7.76b$ into Eq. 7.78 shows that the latter is indeed correct.  The transmitted power is eqlwl to the incident power minus the reflected power.  

In view of Eqs. 7.14 and $7.76a$ , it is clear that a generalized reflection coefficient can be defined for situations involving uniform plane waves at normal incidence upon plane boundaries.  By analogy with trans­ mission lines, we write  

$$
\begin{array}{r}{\tilde{\Gamma}(z)\equiv\frac{\mathbf{E}_{x}-\left(z\right)}{\mathbf{E}_{x}+\left(z\right)}=\frac{\mathbf{E}_{x0}-e^{j\beta_{0}z}}{\mathbf{E}_{x0}+e^{-j\beta_{0}z}}}\\ {=~\bar{\Gamma}(0)e^{j2\beta_{0}z}\qquad\qquad\qquad\qquad\qquad\quad}\end{array}
$$  

We then define a normalized impedance $\mathbf{Z}_{n}(z)$ by the relation  

$$
\mathbf{Z}_{n}(z)\equiv\frac{1+\bar{\Gamma}(z)}{1-\bar{\Gamma}(z)}
$$  

But by Eqs. 7.79 and 7.14 we can re-express $\mathbf{Z}_{n}(z)$ of Eq. 7.80 in the form  

$$
{\bf Z}_{n}(z)=\frac{\mathrm{E}_{x0}{}^{+}e^{-j\beta_{0}z}+\mathrm{E}_{x0}{}^{-}e^{j\beta_{0}z}}{\mathrm{E}_{x0}{}^{+}e^{-j\beta_{0}z}-\mathrm{E}_{x0}{}^{-}e^{j\beta_{0}z}}=\frac{\mathrm{E}_{x}}{\eta\mathrm{H}_{y}}
$$  

It is often convenient, but by no means necessary, to regard $\pmb{\eta}$ as a "characteristic impedance," in which case the unnormalized impedance $\mathbf{Z}(z)$ becomes equal to what we have previously called the wave im­ pedance looking in the $+z$ direction:  

$$
\mathbf{Z}(z)\,=\,\mathbf{Z}_{z}\,\equiv{\frac{\mathrm{E}_{x}}{\mathrm{H}_{y}}}\,\mathrm{ohms}
$$  

It is on this basis, in fact, that we have made the transmission-line representations in Figs. 7.9 and 7.12.  

In any case, simply on the strength of Eqs. 7.79, 7.80, and 7.81, the entire set of procedures for transmif:'sion lines becomes applicable to these uniform plane-\Yaye problems.  In particular, the Smith chart (and others) can be used to great ad\"antage instead of dealing directly with the boundary conditions at interfaces.  The next section illus­ trates the techniques.  

# 7.3.3  Normal Incidence on Multiple Dielectrics  

Consider the problem of a sheet of dielectric of thickness $\imath$ , upon one side $(z\,=\,-l)$ of which is incident  normally from $z=-\infty$ an $_x$ ­ polarized uniform plane ,,"a'"e (Fig. 7.15).  Our interest might be in the percentage of the inci(Ient po\yer ,,"hich is reflected for various values of $\iota$ , giwn the frequency nmi the dielectric constant $\epsilon_{2}>\epsilon_{0}$ .  

$\Lambda$ straightforward nttack on the problem would require consideration of the five waws shmYl1, and then a matching of tangential electric antI magnetic fields at the two interfaces $z=0$ and $z=-l$ to determine the amplitudes of the four unknown ,,"aves.  Since, however, the wave propagation within each medium obeys transmission-line equations, and since the boundary conditions of continuity of tangential el ectric and magnetic fields are exactly like the continuity conditions of voltage and current at a line termination, the problem may be reduced to that shown in Fig. 7. W.  

![](images/9d51dbd23dea436e22a9b90ccdb861c149295b61ecc29fbaf39468c35f042a74.jpg)  
Fig. 7. 1 5.  A multiple-interface problem.  

We wish to find the magnitude of the reflection coefficient on line 1 , which requires that w e  determine the impedance Z normalized on the characteristic impedance $\eta_{0}$ '  For definiteness, let $\epsilon_{2}=4\epsilon_{0}$ , and sup­ pose that the frequency is such that the wayc length $\lambda_{0}$ in air is $3~\mathrm{cm}$ . The wave length in the dielectric medium (line 2) is then $\lambda_{2}=\,\%\times3$ $=1.5~\mathrm{{cm}}$ .  

We sec at once that, if $l\,=\,\mathfrak{H}_{2}\uplambda_{2}\,=\,0.75\;\mathrm{cm}$ (or any intep;er multiple thereof) , line 2 becomes a half-wa\'e line and $\sf{Z}=\eta_{0}$ .  Then line 1 is matched, and th ere is n o  refleetion at all.  There wilI, howe"er, he re­ flections for other \':llues of $l.$ .  

From the point of view of line 2, the normalized loael impedance a t $z=0$ L'5 $\eta_{0}/\eta_{2}\,=\,\sqrt{\epsilon_{2}/\epsilon_{0}}\,=\,2,$ , sl!mm at point $\varLambda$ in Fig;. 7. 17.  A s $\imath$ is inere[lsecl from zero, the Smith chart shows that $\mathbf{Z}/\eta_{2}$ becomes i3mallest in magnitude and real at point $B$ , when $l\,=\,\textstyle{\frac{1}{74}}\lambda_{2}\,=\,0.375\;\mathrm{cm}$ .  Its smallest value is 0.5.  From the point of vic\\' of line 1, the normalized load impedance is $\mathrm{Z/\eta_{70}\,=\,(Z/\eta_{2})\,(\eta_{2}/\eta_{0})\,=\,\Sigma_{2}(Z/\eta_{2})}$ , \\'hidl traces the dashod circle on tho chart passing through t ho rca l axis at normalized resistancc valuos 0.2;) allli 1 .0 \\"holl $l\,=\,\%\lambda_{2}$ and $l\,=\,0$ (poillts $\boldsymbol{C}$ anc! $D$ ) rc"pcdin ly.l  Thc largest rcflection cocfli('icnt 0 1 1  lillc 1 thus o c c urs whon $l\,=\,\dag\!_{4}\lambda_{2},$ and has tho value  

![](images/42d5ce63c467ce44c4871eeff70a7600cae69f92510a3c4d8d6a6b92810d6f2d.jpg)  
Fig. 7. 1 6.  Transmission-line equivalent of Fig. 7. 15.  

![](images/3d023e716405989487260252b5a3a49fd87065bb1b1b2d2058d83f82cb7e8759.jpg)  
F i g .  7. 1 7.  Smith chart for the example of Figs. 7. 1 5  and 7. 16.  

$$
|\,\bar{\Gamma}\,|_{\mathrm{mux}}=\frac{1-0.25}{1+0.25}=\frac{3}{5}=0.6
$$  

Thus the maximum percentage reflected  pO\\'or is $\left|\;\bar{\mathrm{I}}^{\dagger}\right|_{\mathrm{mix}}^{2}=9/2\bar{\mathrm{o}}=$ 0.3G,  or $30\%$ , "'holl $l\,=\,0.375\;\mathrm{{cm}}$ (or an  odd mult iple thercof) . For the case $l\,=\,_{\!}^{1}\AA\lambda_{2}\,=\,0.18\overline{{{\,}}}\bar{\mathrm{\footnotesize~\textmu~}}(\mathrm{m}$ , the Smith chart shmni $\mathtt{Z}/\eta_{2}=$ $0.8\mathrm{~-~}j0.6$ at point $\emph{E}$ .  X ormalized 011 $\eta_{0}$ , to  refer to line 1 ,  this be1 That the dashed locus 1Ililst ue a eircle folIo\\'  from  cc. 3.5,  Eq. 3.7V ff., and the reference cited there.  

comes $0.4\mathrm{~-~}j0.3$ (point $\pmb{F}$ ), which lies on the dash-dot circle of con­ stant ${\big|}\,{\bar{\Gamma}}\,{\big|}$ passing through  normalized resistance values 0.3G and 2.78.  Thus the standing-wave ratio on line 1 is $s=2.78$ , and $|\,\bar{\mathbf{I}}\,|\,=$ 88  --+  11-    = 1.78/3.78 = 0.471.  This corresponds to (0.471)2 or 22.2% reflected power.  

Needless to say, since the dielectric is lossless, the power transmitted into medium 3 (Fig. 7. 15) is equal to the difference between the in­ cident and reflected powers in medium 1.  Expressed as a percentage of the incident power, that transmitted in our numerical example is $100\%$ for $\iota=0$ (or $l=\uplambda_{2}/2\uplambda$ , $77.8\%$ for $l=\uplambda_{2}/8,$ , and a minimum of $64\%$ for $l=\uplambda_{2}/4$ .  

Perhaps it is worth while to see the analytical treatment of the prob­ lem of Fig. 7.15 (or the equivalent in Fig. 7.1G), if only to appreciate the simplification available from the previous Smith-chart solution. Thus, for medium 2 at $z=0$ , we have  

$$
\Gamma_{R2}=\frac{\eta_{0}-\eta_{2}}{\eta_{0}+\eta_{2}}
$$  

since $\Gamma_{R2}$ is real here.  At $z=-l$ , however,  

$$
\bar{\Gamma}_{2}(-l)\,=\,{\Gamma}_{R2}e^{-j2\beta_{02}l}
$$  

The corresponding normalized impedance in medium 2 at $z=-l$ is  

$$
\frac{\mathrm{~Z~}}{\eta_{2}}=\frac{1+\bar{\Gamma}_{2}(-l)}{1\,-\,\bar{\Gamma}_{2}(-l)}=\frac{1+\,\Gamma_{R2}e^{-j2\beta_{02}l}}{1\,-\,\Gamma_{R2}e^{-j2\beta_{02}l}}
$$  

But the wave impedance $\mathbf{Z}$ in ohms must look the same at $z=-l,$ , whether we consider ourselves to be just in medium 1 or just in medium 2.  This is, in fact, a direct result of the boundary condition requiring tangential $\mathbf{E}$ and tangential II to be separately continuous across the interface.  In the transmission-line analogy (Fig. 7.1G), the continuity of $\mathbf{Z}$ follows likewise from the separate continuity of voltage and cur­ rent.  Thus the normalized load impedance seen by medium 1 at $z=$ $-\imath$ is  

$$
\frac{\mathrm{~Z~}}{\eta_{0}}=\frac{\eta_{2}}{\eta_{0}}\biggl(\frac{\mathrm{Z}}{\eta_{2}}\biggr)=\frac{\eta_{2}}{\eta_{0}}\biggl(\frac{1+\,\Gamma_{R2}e^{-j2\beta_{02}l}}{1-\,\Gamma_{R2}e^{-j2\beta_{02}l}}\biggr)\,
$$  

leading to a load reflection coefficient in medium 1 at $z=-l$ of  

$$
\bar{\Gamma}_{R1}\,=\frac{(\mathrm{Z}/\eta_{0})\,-\,1}{(\mathrm{Z}/\eta_{0})\,+\,1}=\,\Gamma_{R2}\left(\frac{e^{j2\beta_{02}l}\,-\,1}{{\Gamma_{R2}}^{2}\,-\,e^{j2\beta_{02}l}}\right)
$$  

where a considerable amount of algebra has been omitted ,yhich the reader is urged to reproduce on a separate sheet.  

Now "'e ure interested in $|\,\bar{\Gamma}_{{\/R}1}\,|^{2}$ , which can be found most easily from sketches showing the geometry of the complex numbers in the numerator and denominator of $\bar{\Gamma}_{\!{\cal R}1}$ .  'Ye find  

$$
|\,\bar{\Gamma}_{R1}\,|^{2}=\frac{4\,{\Gamma_{R2}}^{2}\sin^{2}\beta_{02}l}{(1\,-\,{\Gamma_{R2}}^{2})^{2}+\,4\,{\Gamma_{R2}}^{2}\sin^{2}\beta_{02}l}
$$  

Evidently $\vert\,\bar{\Gamma}_{\!R1}\,\vert\,=0$ if $\beta_{02}l\,=\,0,\,\pi,\,2\pi,\,\cdots,$ i.e., the medium thick­ ness $\iota$ is an integer multiple of $\uplambda_{2}/2$ .  Also it is cleur that the whole fraction is largest (as a function of $\iota$ ) \yhen $\sin^{2}\beta_{02}l$ is largest, i.e., when $2\beta_{02}l\,=\,\pi,\,3\pi,\,5\pi,\,\cdot\cdot\cdot$ or $l=\uplambda_{2}/\t,\uplambda_{3}/\t,\updelta\uplambda_{2}/\t$ , etc.  Under this con­ dition the (maximum) value of $\left|\,\bar{\Gamma}_{{\/R}1}\,\right|$ is  

$$
|\,\bar{\Gamma}_{R1}\,|_{\mathrm{max}}=\frac{2|\,\Gamma_{R2}|}{1+|\,\Gamma_{R2}|^{2}}
$$  

In our numerical example, "'here $\eta_{0}/\eta_{2}\,=\,2_{\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\,$ , \\'e haye $\Gamma_{R2}\,=\,(2\,-\,1)/$ $\left(2+1\right)\,=\,\stackrel{1}{,}\,\left<\,3$ .  Hellce $|\,\bar{\Gamma}_{\!R\,1}\,|_{\mathrm{\scriptsize{mux}}}\,=\,_{\!\gamma\,3}^{2}/(1+\scriptstyle\frac{1}{/9})\,=\,_{\!\gamma\,3}^{3},$ , a s  found previ­ ously from the Smith-ehart solution.  

If the polarization of the inridcnt waye were along the $\mathcal{Y}$ -axis, our previous  work  would  rcmain c"sentially unchanged.  In fact,  the simplest procedure \\'CHlld be to relabel the  axes so that $\mathcal{Y}$ bccame $_x$ and $-x$ became $\mathcal{Y}$ .  Sin('e the houndary conditions are not affected physically by the direction of the electric field in the $x,y$ plane, the formal solution of the problem thCll remains completely umhangcd.  

In the sinusoidal st eady state at frequelH'Y $\omega$ , the comments about polarization ma(1c in  :;:ee.  7. 1 .-1  aIHI Sec.  1.3.2 mean that the mo"t general incident \\'a\'C might  simply 11a\'e an ${\mathrm{F}_{,x0}}^{+}$ and an ${\mathrm{I}\!\!:}_{y0}{}^{+}$ of different magnitudes and phases.  Thus "'e would make  (and latcr superpose) two solutions to our problem, the difference bet\\'('en t1H';;e solutions being only a $+\mathfrak{j}0^{\circ}$ rotation about the $+z$ -axis and a magni­ tude and phaf'e d ifference corresponding to tllOse of $\mathrm{F}_{x0}{}^{+}$ and ${\mathrm{I}\mathrm{:}}_{y,0}+$ .  

An interesting prnetical example of trnnc:mission-line thinkinp; a p­ plied to plane-\Ya\'e problems is that of "coated optics."  If, in Fig. 7 . 1 5, medium 3 were glass rather than air-representinp; a lens or show "'indO\\'-and medium 1 \yere  still air,  olle might ask for a coating (medium 2) which "'ould match $\eta_{3}$ to $\eta_{0}$ and thereby cIiminate obj ec­ tionable reflectiolls from the front s urface.  One solution would be [\, quarter-wave coating aeting as [\, matchinp; transformer \"hose charac­ teristic WH\"e impedance $\eta_{2}$ would have to satisfy the relation $\eta_{2}=$ $\sqrt{\eta_{0}\eta_{3}}$ .  Such materials exist for visible-light mwe lengths, and are used on some optical-instrument lenses.  It is important to note that the thickne o must be a quarter of a \\":1\"e length as measured in the coatino material itself, not of the \\'a \Oe length in glass or air.  Moreover, the matehi ng i whavior of the coating is exact only at the single fre­ quency for \\'hieh the film is a quarter wave thick, and when the light wan's r-trike it at normal ineidence.  

Before Ica\Oi ng the topic of uniform plane wayes at normal ineidence in losskss med ia, we should mcntion that t he rather complete analogy of ther-e prohlems to thosc of lossless t ran:-;mission lines appl ies in the time domain, for transients, as ,,"ell as  ill the frequen("y domain for r-inusoidal st('ady st at e.  This is c,"idcnt eith('1" directly from Eq;:;. 7.3, 7..1 , and 7.S or from a Fourier point of vic\\" applied to Oll!" results for the steady state.  As long as the charaeieristic impe(la n('e $\eta\,=\,\sqrt{\mu/\epsilon}$ and phase Ycloeity $v_{p}\,=\,1/\sqrt{\epsilon\mu}$ ; ;.are independent of frequeney, the steady-sta t e  idea of independent $(+)$ and $(-)$ \\"ayes propagating with corre:-ponding time delays proportional to distance, mH] with voltage­ t o-current ratios $\pmb{\eta}$ and $-\eta$ r('spe<.:tin ly, <.:arries oyer directly into the time domain.  Only the question of rotating polarizations is slightly new ; but since such  ituatiolls ean al"ouys be n  ohoed into two r,;eparate linear polarizations, the difficulty amounts merely to solvi ng t\yice as many of the same old prohlems.  

Transmission-line analogies are present, but more subtle, in our next topics, \\"hich begin with oblique incideJ1('e upon plane boundaries and conclude wiih some examples of guided waves.  

# 7.4  Oblique Incidence of a Uniform Plane Wave  

# 7.4. 1  Geometry of Oblique Incidence  

"Te already know that a uniform plane \\"aYe propagating in any space direction is a solution to l\Tax,,"e!\'s equations, and that it can always be decomposed into two linearly polarizc(l components with mutually perpendicular electric  (and magnetic)  fields.  These facts ha\"e not really helped us greatly in our consideration of normal in­ cidenee, for two reasons :  

1. The direct ion of propagation of the incident wave could always he chosen as the $\textit{\textbf{z}}$ -axis, and the normal to the plane boundary would coincide with it (as wouhl the direct ion of propagation of the reflected and trunf'mitted \\"an·s) .  

2.  The polarizat ion of the incident wa\OC could not only be considered linear but also its orientation needed  little attention because of the uniform electrical structure and symmetrical orientation of the bound­ ary with respect to the $\pmb{z}$ -axis.  

"'hen ,,'e come to oblique incidence, however, the questions of direc­ tion of propagation and polarization are by no means trivi:ll physically. Therefore we must acknowledp;e them in our analysis.  

The geometry for a uniform plane wave at oblique incidence upon a uniform plane boundary is showll in Fig. 7.18,  The unit vector $\pmb{n}_{1}$ , normal to the boundary, and the propagation yedor $\upbeta_{0i}$ of t h e  incident ,,'ave define \\"hat is called the plane oj incidence.  The angle oj incidence $\vartheta_{i}$ is measured in this piane as the acute angle bet\\'een $-\upbeta_{0i}$ and $\pmb{\nu}_{1}$ ' $\Lambda$ unit vedor $\pmb{\nu}_{2}$ ,  normal to the plane of incidence, is also parallel to the boundary plane,  

Now the electric alHI magnetic field vedors of the incident wave must lie in planes perpcmlicular to its propagation vector $\upbeta_{0i}$ .  There is only one diredion in space \\'hich is parallel to these plancs and also parallel to the boundary p lane.  This direction is dcfined by the unit vector $\pmb{n}_{2}$ , normal to both $n_{1}$ and $\upbeta_{0i}$ .  "'e shal l make the $+x$ -axis parallel to $\pmb{n}_{2}$ . For the $+z$ -axis \\'e shall chou:-<e the line llormal to thc boundary plane, i.e., that defincd by $-\pmb{n}_{1}$ .  Thc $y$ -axis is finally determincd by the line pcrpendicular to $\pmb{n}_{2}$ aIHI $\pmb{\nu}_{1}$ in :-<uch a sCIl:-<e that it forms a right-hamled coordinate :-<,rslcm with the $+z-$ ami $+x.$ -axcs.  The $+y.$ -axis is therefore in the direc t ion $(-\pi_{1})\ \times\ n_{2},$ p:lralle1 to both thc boundary planc ancl the plane of incidenl:e.  

It should now be clear that the cledrie and magnetic fields of the incident Wl1\'e, \\'hidl are mutually perpendicular  and  lic in a plane nor mal to its directioll of propagation ,  cannot uoth also be parallel (tDJlgential) to the boundary.  Thus, thc simplcst polarizations we can have, from the point of view of meeting boundary conditions on tan­ gential field components, arc those for "'hich either $E_{i}$ or $\boldsymbol{{\cal I}}\!\!\!/\!\boldsymbol{\phantom{.}}$ is linelll'ly polarized along the $x$ -axis $\left(\pmb{{\eta}}_{2}\right)$ .  Thell either $E_{i}$ or $\pmb{I}\pmb{I}_{i}$ (but not both) becomcs parallel to the boundary plane.  Since $E_{i}$ and $\boldsymbol{I}\boldsymbol{I}_{i}$ arc always mutually perpendicular in a  linearly polarized uniform plane mlVe, these two cases, in fact,  also represent two mutually perpendicular electric-field polarizations of the incident wave.  Therefore, if for every $\vartheta_{i}$ \ye trent these two cases, we shall be able to handle alI possibilities through subsequent use of superposition.  

![](images/c5d428095f9c9fff1ee764c58375e0d312ad8fa02c808c11bfee64877eba2c20.jpg)  
Fig. 7.1 8.  Geometry of oblique incidence.  

![](images/934cda0a6c005491b42bb9d34185bc440bde72c4a9f6cd478ac5f8abf4b17d7b.jpg)  
Fig.  7.1 9.  Rotal'ion  of  coordinates for a uniform plane wavo.  

Our choice of the $^z$ -axis normal to the boundary surface means that it neither coincides with the direction of propagation of the incidcnt waye nor, in gcneral, " 'ith that of the rcflected or transmitted ,,·aves.  This leaves us with the task of cxpressing analytically the field of a uniform plane wave in a rotated coordinate system, a problem which we have discussed previously in connection ,,·ith Figs. 7.2 and 7.7.  

In the present case, consider the wave propagating along the $+z^{\prime}$ direction in Fig. 7. 1\:), and take the polarization (direction of $\pmb{{\cal E}}$ ) to be linear and along the $+x$ -axis, ,yhich points out of the paper.  The com­ plex vector E will then also be along the $+x$ -axis, and the magnctic field \yill be along the $+y^{\prime}$ axis, as shown.  In the $(x,\,y^{\prime},\,z^{\prime})$ coordinates, which are the familiar ones, we have  

$$
{\begin{array}{l}{\mathbf{E}=a_{x}\mathrm{{E}}e^{-j\beta_{0}z^{\prime}}}\\ {\mathbf{II}=a_{y^{\prime}}\mathrm{{II}}e^{-j\beta_{0}z^{\prime}}}\\ {\mathbf{H}={\frac{\mathbf{E}}{\eta}}}\end{array}}
$$  

![](images/7d502919490f5c2423e23bf3f3885ea1da338cf603865d7edeebe37788bb05eb.jpg)  
F i g .  7.20.  A uniform plane wave moving along the $+z^{\prime}$ direction.  

For the new coordinates $(x,\,y,\,z)$ of Fig. 7. 10, the $_x$ -axis has remained unchanged, but the others have been rotated by the angle $\vartheta$ defined on the sketch.  Therefore, to express unit vector $\pmb{a}_{y^{\prime}}$ in terms of unit vectors ${\pmb{a}}_{\pmb{y}}$ and $\pmb{\alpha_{z}}$ , we have from the geometry  

$$
\mathbf{a}_{y^{\prime}}=a_{y}\cos{\vartheta}+a_{z}\sin{\vartheta}
$$  

Comparing Fig. 7.10 with Fig. 7.2 in regard to $z^{\prime}$ , we note that in Fig. 7.19  

$$
l_{z^{\prime}}\,=\,0\qquad m_{z^{\prime}}\,=\,-\sin\vartheta\qquad n_{z^{\prime}}\,=\,\cos\vartheta
$$  

so that from Eq. 7.19 there follows the relation  

$$
z^{\prime}=\,z\cos\vartheta\,-\,y\sin\vartheta
$$  

Consequently Eqs. 7.83 become  

$$
\begin{array}{r l}&{\mathbf{E}=a_{x}\mathrm{E}e^{j\beta_{0}y\sin\vartheta}e^{-j\beta_{0}z\cos\vartheta}}\\ &{\mathbf{II}=(a_{y}\mathrm{II}\cos\vartheta+a_{z}\mathrm{II}\sin\vartheta)e^{j\beta_{0}y\sin\vartheta}e^{-j\beta_{0}z\cos\vartheta}}\\ &{\mathbf{II}=\cfrac{\mathbf{E}}{\eta}}\end{array}
$$  

which should be compared with Eqs. 7.2G and $7.32a$ .  Observe particu­ larly the relationship between the vector components of II in Eq. $7.86b$ amI the correspomling geometric representation of them in Fig. 7. 19.  Obviously this part of II could be written by inspection from the figure.  The same is true of the exponential factors in Eqs. $7.86a$ and $7.86b$ . $\Lambda$ special case of Fig. 7.3& for the present situation is shown in Fig. 7.20.  The corresponding form of Eqs .  7.33 through $7.36\mathrm{\may}$ be written in view of either Eqs. 7.85a or, preferably, of the geometry of Fig. 7.20 directly :  

# 350  ELECTROMAGNETIC ENERGY TRANSMISSION AND RADIATION  

$$
\uplambda_{y}\equiv\frac{\uplambda}{\sin\vartheta}=\frac{2\pi}{\beta_{0}\sin\vartheta}\equiv\frac{2\pi}{|\beta_{y}|}
$$  

$$
\uplambda_{z}\equiv\frac{\uplambda}{\cos\vartheta}=\frac{2\pi}{\beta_{0}\,\cos\vartheta}\equiv\frac{2\pi}{|\beta_{z}|}
$$  

$$
\vert\beta_{y}\vert=\beta_{0}\sin{\vartheta}
$$  

$$
|\beta_{z}|=\beta_{0}\,\cos\vartheta
$$  

$$
{\begin{array}{l}{\displaystyle v_{y}\equiv{\frac{\omega}{\,|\beta_{y}|\,}}={\frac{\omega}{\beta_{0}\sin\vartheta}}={\frac{\vartheta}{\sin\vartheta}}}\\ {\displaystyle v_{z}\equiv{\frac{\omega}{\,|\beta_{z}|\,}}={\frac{\omega}{\beta_{0}\sin\vartheta}}={\frac{\vartheta}{\cos\vartheta}}}\end{array}}
$$  

# and because $\sin^{2}\!\vartheta+\cos^{2}\!\vartheta=1,$  

$$
\beta_{z}^{~2}+\beta_{y}^{~2}=\beta_{0}^{~2}
$$  

$$
{\frac{1}{{\lambda_{z}}^{2}}}+{\frac{1}{{\lambda_{y}}^{2}}}={\frac{1}{\lambda^{2}}}
$$  

$$
{\frac{1}{{v_{z}}^{2}}}+{\frac{1}{{v_{y}}^{2}}}={\frac{1}{v^{2}}}
$$  

It should be cmphasized in connection ,yjth Fig. 7.20 that when the actual wave moves in the arrow directions as time goes on, the phase fronts advance along $+z^{\prime},\,+z,$ and $-y$ o  This accounts for the dif­ ferent signs of the exponents containing $\pmb{z}$ and $\boldsymbol{y}$ in Eqs. 7.8G.  

If  the  plane wave had  the alternate  linear polarization  (i.e., II parallel to the boundary) but still propagated in the $+z^{\prime}$ direction, it could have E along $+y^{\prime}$ and II along $-x$ :  

$$
\begin{array}{l}{{\displaystyle{\bf E}\,=\,a_{\nu};\!\!\mathrm{E}e^{-j\beta_{0}z^{\prime}}}\ ~}\\ {{\displaystyle{\bf I I}\,=\,-a_{x}\mathrm{II}e^{-j\beta_{0}z^{\prime}}}\ ~}\\ {{\displaystyle{\bf I I}\,=\,\frac{\mathrm{E}}{\eta}}}\end{array}
$$  

In the $(x,\,y,\,z)$ coordinates, Eqs. 7.Q l become  

$$
\begin{array}{r l}&{\mathrm{\bf~E}=(a_{y}\mathrm{E}\cos\vartheta+a_{z}\mathrm{E}\sin\vartheta)e^{j\left|\beta_{y}\right|y}e^{-j\beta_{z}z}}\\ &{\mathrm{\bf~II}=-a_{x}\mathrm{I}\mathrm{I}e^{j\left|\beta_{y}\right|y}e^{-j\beta_{z}z}}\\ &{\mathrm{\bf~II}=\displaystyle\frac{\mathrm{\bf~E}}{\eta}}\end{array}
$$  

It is extremely desirable to learn to write equations like Eqs. 7.8G and 7.92 directly from pictures of the E and I I  vectors (in the manner of Fig. 7. 19) and of the phase fronts  (in the manner of Fig. 7.20) . Such  pictures  are  surprisingly  helpful  in  resolving  ambiguities  of algebraic sign connected ,dth the field components and the propaga­ tion exponents along the coordinate axes.  A thorough mastery of these malters now will l'emove the major difficulties from the forthcoming discus­ sions.  

'Ye arc now in a position to examine reflection and refraction of uniform plane waves at ohlique incidence upon the interfaee between lossless media.  

# 7.4.2  Oblique Incidence upon a Perfect Conductor  

First ,\"e may consider the perfectly conducting metal mirror at $z=0$ in Fig. 7.2 1, upon which is incident an $x^{\th}$ -polarized wave from a direction $\vartheta_{i}$ with the normal.  Since no field exists within the metal, we have only to deal with a possible reflected wave.  1\1oreover, inasmuch as the incident wave has its electric field parallel to the conducting plane, and the boundary eondition requires the total electric  field parallel to that plane at $z\,=\,0$ to vani:;h, it is elear that the reflected wave will have the same polarization as the incitlcnt wave.  lIenee the direction of propagation of the rcflected wave will lie in the plane of incidence, as shown in Fig. 7.21, at some angle $\vartheta_{r}$ with respect to the bOllndary normal.  

![](images/e62e59edfd656475c512a2708474579cf2298c0034334a4f344197a4fcd89a73.jpg)  
Fig. 7.2 1 .   Obliquc  incidence upon a perfect conductor with pohri7.al ion  pam\ld  to  thc boundary.  

# 352  ELECTROMAGNETIC ENERGY TRANSMISSION AND RADIATION  

The incident wave is given as  

$$
\begin{array}{l}{{\displaystyle{\bf E}_{i}=a_{x}\mathrm{E}_{i}e^{j\beta_{0}y\sin\vartheta_{4}}e^{-j\beta_{0}z\cos\vartheta_{4}}}\ ~}\\ {{\displaystyle{\bf I I}_{i}=(a_{y}\frac{\mathrm{E}_{i}}{\eta}\cos\vartheta_{i}+a_{z}\frac{\mathrm{E}_{i}}{\eta}\sin\vartheta_{i})e^{j\beta_{0}y\sin\vartheta_{i}}e^{-j\beta_{0}z\cos\vartheta_{4}}}\ ~}\end{array}
$$  

and the reflected wave is of the form  

$$
\begin{array}{l}{{\displaystyle{\bf E}_{r}=a_{x}\mathrm{E}_{r}e^{j\beta_{0}y\mathrm{\,sin}\,\vartheta_{r}}e^{j\beta_{0}z\cos\vartheta_{r}}}\ ~}\\ {{\displaystyle{\bf I I}_{r}=\left(-a_{y}\,\frac{\mathrm{E}_{r}}{\eta}\cos\vartheta_{r}+a_{z}\,\frac{\mathrm{E}_{r}}{\eta}\sin\vartheta_{r}\right)e^{j\beta_{0}y\sin\vartheta_{r}}e^{j\beta_{0}z\cos\vartheta_{r}}}\ ~}\end{array}
$$  

At $z=0$ , for all $\emph{y}$ (and $\overrightharpoon{x}$ ), we require ${\bf E}_{i}+{\bf E}_{r}=0$ ;  i.e.,  

$$
\mathrm{E}_{i}e^{j\beta_{0}\upsilon\;\mathrm{sin}\;\vartheta_{i}}=\;-\mathrm{E}_{r}e^{j\beta_{0}\upsilon\;\mathrm{sin}\;\vartheta_{r}}
$$  

so  

$$
\begin{array}{r}{\vartheta_{r}=\vartheta_{i}(\equiv\vartheta)}\\ {-\mathrm{E}_{r}=\mathrm{E}_{i}(\equiv\mathrm{E})}\end{array}
$$  

Equation $7.96a$ is the familiar optical law that the angles of incidence and reflection are equal.  From Eq. 7.96b we see that all the incident power is reflected.  

The total field for $z\leq0$ is giyen by the sum of the incident and re­ flected wayes under conditions of Ell. 7.96.  

$$
\mathbf{E}\,=\,-\,a_{x}2j\mathrm{{E}}e^{j\beta_{0}y\,\sin\,\vartheta}\,\sin\,\left(\beta_{0}z\,\cos\,\vartheta\right)
$$  

$$
{\bf I I}=\frac{2\mathrm{E}}{\eta}\,[a_{y}\cos\vartheta\,\cos\,(\beta_{0}z\,\cos\vartheta)\,-a_{z}j\sin\vartheta\,\sin\,(\beta_{0}z
$$  

$$
\cos\vartheta)]e^{j\beta_{0}\upsilon\sin\vartheta}
$$  

We observe that $\mathrm{{\calI}}\!_{x}$ and $\Pi_{y}$ arc $90^{\circ}$ out of time phase.  This is to be expected on the basis that the $\pmb{z}$ component of the complex Poynting vector is $\mathrm{}^{1}\!/\!\!/\mathrm{E}_{x}\mathrm{II}_{y}{}^{*}$ , ,yhich cannot have a real part because no average power is absorbed by the mirror.  It is also note\yorthy that $\mathrm{{\calE}}_{x}=0$ whenever $\beta_{0}z\,\cos\vartheta\,=\,-m\pi,\,m\,=\,0,\,1,\,2,\,\cdot\,\cdot\,;$ or  

$$
z=\frac{-m\lambda}{2\cos\vartheta}=~-\,\frac{m\lambda_{z}}{2}\,\qquad m\,=\,0,\,1,\,2,\,\cdots
$$  

The electric field has nodal pl::l.I1es parallel to the mirror at multiples of $\frac{1}{2}\lambda_{z}$ from it.  Observed along $\textit{\textbf{z}}$ , all the field components have standing­ wave character; but $\mathrm{{\calE}}_{x}$ and $\mathrm{II}_{z}$ have nodes at the same planes, while  

# Fig. 7.22.  Transmission line analogy for the z dependence and the $\pmb{x}$ and $\pmb{y}$ fichl com­ ponents in Fig. 7.21.  

![](images/39428e7147e06f58e4d9df01e0060e6c8e62eee9cee8f1edeb0dfcd93fea0acf.jpg)  

the nodes of $\mathrm{{II}}_{y}$ arc displaced $\%h_{z}$ from those of $\mathrm{E}_{x}$ and $\mathrm{II}_{z}$ .  The $y$ variation of all the ficltl components, on the other hand, hfls traveling­ wavc character \\·ith cffecti\·c wave length $\lambda_{y}$ and propagation in the $-y$ direction.  This fact cheeks with the $\emph{y}$ component of the complex Poynting vector $(-{\textstyle\frac{1}{\sqrt{2}}}\mathrm{E}_{x}\mathrm{II}_{z}{}^{*})$ , \\'hich is real and negative, indicating average power flowing in the $-y$ direction.  

It is therefore convenient to think of the whole field as a pure stand­ ing wave extending along $-z$ ,  which, hO\\,ever, also "slides" bodily along $-y$ o  Indeed, \\'e note that the field components parallel to the mirror are  

$$
\begin{array}{l}{\displaystyle\mathrm{E}_{x}=\left[-2j\mathrm{E}\sin\left(\frac{2\pi z}{\lambda_{z}}\right)\right]e^{j(2\pi y/\lambda_{y})}\,}\\ {\displaystyle\mathrm{II}_{y}=\left[\frac{2\mathrm{E}}{\left(\eta/\cos\vartheta\right)}\cos\left(\frac{2\pi z}{\lambda_{z}}\right)\right]e^{j(2\pi y/\lambda_{y})}\,}\end{array}
$$  

\\'hich, examined along $_z$ at fixed $\emph{y}$ , look exactly like the voltflge and curren t standing waves on the transmission line of Fig. 7.22.  Of course, \ye sec from Eqs. 7.03 and 7.01 that this line shows only some of the features of the actual problem inasmuch as it omits all information relating to the traYCling-wave nature of the $\emph{y}$ dependence, and to the corresponding magnetic  field  component $\mathrm{II}_{z}$ .  Nevertheless,  such partial equivalence is often useful.  It is hO\\'ever most important to remember that both the characteristic impedance of the line and its phase constant involve the angle of incidence.  It is not hard to sec why this is so, if we look back at just the incident wave in Fig. 7.21. Whereas $(\|\ \mathbf{E}_{i}\|/\|\ \mathbf{II}_{i}\|)\,=\,\eta,^{1}$ our transmission line deals only with $|\mathbb{E}_{x i}|/|\,\mathrm{II}_{y i}|$ ,  i.e. , only with the $+z$ -directed wave impedance $\mathbf{Z}_{z}$ '  For the case at hand, $\left|\operatorname{F}_{x i}\right|\,=\,\left\|\ \operatorname{F}_{i}\right\|$ , but $|\operatorname{II}_{y i}|=\parallel\mathbf{II}_{i}\parallel$ cos $\vartheta$ .  Hence the appropriate line impedance is $\eta/\cos\,\vartheta$ f.  Similarly, the appearance of $\beta_{z}\,=\,\beta_{0}\,\cos\vartheta$ is evident from Fig. 7.20, \\'here the wave length ob­ served along $^z$ is seen to be greater than $\uplambda$ by the factor $1/\cos\vartheta$ .  

$1\|\textbf{A}\|{}=\sqrt{\textbf{A}\cdot\textbf{A}^{*}}=\sqrt{|\mathrm{A}_{x}|^{2}+|\mathrm{A}_{y}|^{2}+|\mathrm{A}_{z}|^{2}}=\sqrt{|\mathrm{A}_{r}|^{2}+|\mathrm{A}_{i}|^{2}}$ .  Hence for a linearly polarized vector $\pmb{A}=\mathrm{Re}\,(\mathbf{A}e^{j\omega t})$ , $\|\mathbf{A}\|=\left\{A\right|_{\mathtt{m a x}}$ .  

If these ideas arc umlerstoou, it will be dear that a revision of Fig. 7.21 for the alternate polarization in \yhieh $\mathbf{II}_{i}$ is parallel to the mirror requires that in Fig. 7.22 we exchange $\mathrm{F}_{y}$ for $\mathrm{F}_{x}$ ; $-\mathrm{II}_{x}$ for $\mathrm{II}_{y}$ ; 'YJ cos $\vartheta$ for $\mathrm{{Z_{0}}}$ instead of $\eta/\cos\vartheta$ ;  and $\beta_{\mathrm{line}}\,=\,\beta_{0}\,\cos\vartheta$ , as before.  The reauer is urged n ot only to chcck the:-:e relation:;hips carefully but also to write out completely all the field components and boull(Iary conuitions for this polarization ill the manller of Err:;. 7.93 through 7.98.  

It is signifiC'ant to realize in this connection that the familiar law of reflection $7.96a$ comes directly from the form of the exponential fa('tors ill Eqs. 7.93 and 7.\).! allll, therefore, is not infiuClH'ecl by the polariza.­ tion.  Indeed , it is really qui te obvious from Fig, 7.20 that, since the boundary condition on the fields has to he satisfied for all values of $\boldsymbol{y}$ , (L ncccssary (but not sufficient) cond ition is that all the \\'a" es concerned in the problem have the same pha e constant (or wave length or phase velocity) when measW'ed alun!] the boundary (in the manner of Eqs. 7.87, 7.88, and 7.89).  Only in this \my can the various \\"aves "keep in step" along the interface, so tkl t the remainder of the boundary condi­ tions can be met at more than just a sin gle point on it.  

# 7.4.3 Oblique Incid ence upon an Interface b etween Lossless Dielectrics  

7.4,3.1  POLAHIzxnox PAIL\LLEL TO  TIn;  BOlJXIHHY.  The next example for consideration ill\'ol n s in('idenC'e of a uniform plane wa.ve upon  the interface bebyeen lossless dicledries  (Fig, 7.23) .  The in­ cident wave is $x$ -polarized (parallel tu the boumbry) as shU\\'n, and is given analytically by Eq. 7.\)3.  "\ gaill, it is dcar that the reflected and  transmitted  (refrac'ted)  wa\'c,;  are  abo $x$ -polarized,  so that all propagation dirediolls lie ill the pla ne uf ill(:idence, as indicated by the figure.  

If we are to have any hope uf establishing the necessary con tinuity of tangcntial $\mathbf{\DeltaF}$ and H aero,;s the boundary pia ne $z\,=\,0$ (for all V) , the phase vclocitie:3 of the thrce wn" cs ((s measured alon!] the V axis must be the same in magnitude and sense.  Thus, from the figure [which, for convenience, sho\\'s $\uplambda$ mther than $v\,=\,(\omega\Lambda)/(2\pi)].$ ,  

$$
\frac{v_{1}}{\sin\vartheta_{i}}-\frac{v_{1}}{\sin\vartheta_{r}}
$$  

$$
\frac{v_{1}}{\sin\vartheta_{i}}=\frac{v_{2}}{\sin\vartheta_{2}}
$$  

or  

$$
\vartheta_{r}=\vartheta_{i}\equiv\vartheta_{1}
$$  

$$
\sin\vartheta_{2}=\left({\frac{v_{2}}{v_{1}}}\right)\sin\vartheta_{1}={\sqrt{\frac{\epsilon_{1}\mu_{1}}{\epsilon_{2}\mu_{2}}}}\sin\vartheta_{1}
$$  

Equation $7.100a$ is n gnin the law of reflection nIlll Eq. 7. 100b is the equally well-known optical result ('ailed Snell':: ;Jaw of refraction.  They arise here from that part of the boundary conditions which merely demands that the th ree ,,'aves be "in step" along the interface; thus these laws do not depend upon the polarization.  

![](images/898344a988f68ced337362a0bc9f488ddc9849af630b63ec43167da50d043acd.jpg)  
Fig.  7.23.  Ohlique  incidence  on  an  interface  bf'tw('('n  lossless  dielectrics with puhri7.al ion parallel to int erface.  

The remainder of the required conditions, ho,,'eYer, will involve the specific continuity of $\mathrm{I}\!\!\!\lambda_{x}$ and $\mathrm{II}_{y}$ across the boundary $z=0$ ;  but, since Eq, 7. 100 nlreacly guarantees the common phase velocity of the three waves nlong $\mathcal{Y}$ , it will be sufficient to apply the field continuity con(li­ tion at any single point.  We choose $y=0$ ; so  

$$
\begin{array}{r}{\mathrm{E}_{x i}+\mathrm{E}_{x r}=\mathrm{E}_{x t}}\\ {\mathrm{H}_{y i}+\mathrm{H}_{y r}=\mathrm{II}_{y t}}\end{array}
$$  

But from Fig. 7.23, and the fact that the complete electric and mag  

# 356  ElECTROMAGNETIC ENERGY TRANSMISSI ON AND RADIATION  

netic fields of a uniform traveling plane wave have the ratio $\pmb{\eta},$ Eqs. 7.101 may be recast to read  

$$
\left.\begin{array}{l}{\mathrm{E}_{x i}+\mathrm{E}_{x r}=\mathrm{E}_{x t}}\\ {\frac{\mathrm{E}_{x i}-\mathrm{E}_{x r}}{\left(\eta_{1}/\cos\vartheta_{1}\right)}=\frac{\mathrm{E}_{x t}}{\left(\eta_{2}/\cos\vartheta_{2}\right)}}\end{array}\right\}\,\,\,\,\,\,\,\,\mathrm{\textbf{Eparallel}~t o~b o u n d a r y
$$  

Ehmmating first $\mathrm{E}_{x t}$ and then $\mathrm{E}_{x r},$ we find from Eq. 7.102  

$$
\begin{array}{l}{{\displaystyle{\frac{\mathrm{E}_{x r}}{\mathrm{E}_{x i}}}\equiv\,{\tilde{\Gamma}}_{R}={\frac{Z_{2}-Z_{1}}{Z_{2}+Z_{1}}}\,}}\\ {{\mathrm{E}_{x t}}}\\ {{\displaystyle{\frac{\mathrm{E}_{x t}}{\mathrm{E}_{x i}}}\equiv\mathrm{T}={\frac{2Z_{2}}{Z_{2}+Z_{1}}}}}\end{array}
$$  

where  

$$
\begin{array}{r l}&{Z_{1}=\frac{\eta_{1}}{\cos\vartheta_{1}}=\frac{\mathrm{E}_{x i}}{\mathrm{H}_{y i}}=-\frac{\mathrm{E}_{x r}}{\mathrm{H}_{y r}}\bigg[\qquad\mathrm{E}_{\mathrm{\parallel}}}\\ &{Z_{2}=\frac{\eta_{2}}{\cos\vartheta_{2}}=\frac{\mathrm{E}_{x t}}{\mathrm{H}_{y t}}}\end{array}
$$  

The similarity of Eqs. 7. 103 to those of a transmission-line junction is evident.  The fact that the characteristic impedances $Z_{1}$ and $\scriptstyle\mathbf{Z}_{2}$ are "'ave impedances and, therefore, involve the angles of incidence and refraction CEq. 7. 104) is very important.  The reason for their appearance has been discussed in connection ,,,ith Fig. 7.22.  If we wish to draw an analogous transmission-line system to represent the z dependence of all the waves, as we did in Fig. 7.22, the propagation constants also must contain these angles, because they ,,,ill refer to phases only along the $\scriptstyle z\cdot$ -axis.  In Fig. 7.24, ""e show the line system for this case.  As in Fig. 7.22, it is vital to understand that Fig. 7.2-1 con­ tains no information about either $\mathrm{II}_{z}$ or the $\boldsymbol{y}$ depemlellce of any of the fields in the actual problem.  

![](images/984b7307b56fe9258248437a2751253b7a87b40369859179ef055dda7edc12b4.jpg)  
F i g .  7.24.  Transmission line analogy for the $\pmb{z}$ dependence and the $\pmb{x}$ and $\pmb{y}$ field components in Fig. 7.23.  

It is equally significant that Snell's law (Eq. 7. 100) relates $\vartheta_{1}$ and $\vartheta_{2}$ ; thus a knO\yledge  of either angle is sufficient to determine the parameters of both lines in Fig. 7.2-1, assuming, of course, that we know E and $\pmb{\mu}$ in both media of the phy. ical problem.  

In spite of the fact that some information about the actual physical problem (Fig. 7.23) is absent from the transmission-line system of Fig. 7.2-1, the latter contains the most involved aspects of the situation, and it docs so in a form for \yhich the Smith chart is applicable.  With just a single interface, the adnlllUlges of the transmission-line repre­ sentation arc hardly evident.  Equations 7. 103 arc really all we need in that case.  If there arc several interfaces, hO\\'e\-cr, the problem of determining $\bar{\Gamma}$ at the first one involves considerations like those we encountered in Fig. 7. 15, for which the Smith chart is a grcat help.  In fact, the only added complication in the oblique case is the need to apply Snell's law at each interface to find the directions of the refracted waves in each medium.  If this is done at the start of the problem, the parameters of the transmission line for each medium arc determined in the manner of Fig. 7.2-1.  From here on, the rest of the work follows exactly the usual transmission-line pattern.  

There is one point about the flow of power in the case of oblique in­ cidence which deserves special comment.  In Fig. 7.23, all the waves have components of the Poynting vector along $-y$ o  There is no reason "'hy these components of the power flow should obey the relation that the "incident" power minus that "reflected" equals that "transmitted," for they arc all in the same direction-parallel to the boundary.  On the other hand, all the \\'aves also han components of the Poynting vector along $+z$ .  It is clear in this case that none of the power flowing normal to the boundary in medium 2 can have originated anywhere but as $+z\cdot$ -directed pO\\'er in mcdium 1.  lIenee, for these normal com­ ponents,  we 'lVollld  expect  the aforementioned pO\\'er rebtion.  In particular, the $+z$ -directed incident power is  

$$
\frac{1}{2}\,\mathrm{E}_{x i}\mathrm{H}_{y i}^{\,}\mathrm{*}=\frac{|\,\mathrm{E}_{x i}|^{2}\,\cos\vartheta_{1}}{2\eta_{1}}=\frac{|\,\mathrm{E}_{x i}|^{2}}{2Z_{1}}
$$  

Similarly, the $+z$ -directed reflected power is  

$$
-\,\frac{1}{2}\,\mathrm{E}_{x r}\mathrm{H}_{y r}{}^{*}=\frac{-\,|\mathrm{E}_{x r}|^{2}}{2Z_{1}}
$$  

and that transmitted is  

$$
\frac{1}{2}\,\mathrm{E}_{x\ell}\mathrm{H}_{y\ell}{}^{*}=\frac{|\mathrm{E}_{x\ell}|^{2}}{2Z_{1}}
$$  

# 358  ELECTROMAGNETIC ENERGY TRANSMISSION AND RADIATION  

The "conservation" relation for $+z$ -dircctcd po\\-er therefore rcads  

$$
|\operatorname{E}_{x i}|^{2}-|\operatorname{E}_{x r}|^{2}={\frac{Z_{1}}{Z_{2}}}|\operatorname{E}_{x t}|^{2}
$$  

or, by dcfinition of $\bar{\Gamma}_{R}$ amI $\mathbf{\Delta}^{\mathsf{\Delta}}\mathbf{T}$ ,  

$$
1-|\,\bar{\Gamma}_{\cal R}|^{2}=\frac{Z_{1}}{Z_{2}}|\!\!\,\mathrm{T}\,|^{2}\qquad\mathrm{\bfE}_{\mathrm{\footnotesize~parallel\to\boundary}}
$$  

This is also the conclusion wc woult! rcach from Fig. 7.2-[.  Substitution of Eqs. 7. 103 in to 7. 105 :oho\Y:: ithat the ]a iter is indced true.  

I t  is also truc that thc ratio of total power per unit area in thc reflectcd wavc $[(|\operatorname{E}_{x r}|^{2})/(2\eta_{1})]$ to that in the incident \rave $[(|\mathrm{I};_{x_{i}}|^{2})/(2\eta_{1})]$ is j ust $|\,\bar{\Gamma}_{\mathit{R}}\,|^{2}$ ; but the ratio of the total po\yer per unit area in the tra ns­ mittcd wa \-c $[(\mid\operatorname{F}_{x\ell}|^{2})/(2\eta_{2})]$ to tha t in the incident \Y<t\·c is $(\eta_{\mathrm{2}}/\eta_{\mathrm{l}})\,|\,\mathrm{T}\,|^{2}$ , which by Eq. 7. 105 is obviously not cqual to $1-|\,\bar{\Gamma}_{\mathit{R}}\,|^{2}$ .  The explana­ tion for this result is the olle suggested abO\'e : ,rhile the norlllal com­ ponents  of thc power flo\\' must obey  the  familiar relation het\\'ecn incident, reflected, amI t ransmitted pO\\'crs, the parallel components need not-and, in general, do not-belmye similarly.  lIcnce the lotal power-f1ow-per-unit-arca vedors need not-and , in general, do not­ obey the familiar "conscrvation" relation !  

7.4.3.2  POLAUIZATIO  IX TIm PLAXE OF I"CIDI·;XCE.  The alternate polarization for the problem of Fig. 7.23 places II parallel to the bound­ ary and $\mathbf{\deltaE}$ in the plane of incidence.  As mcntioncd previously, Eqs.  

![](images/7529530e38b2aec53ee1b6af7c03c35473fe424da21e509200d11c068b63ef42.jpg)  
Fig. 7.2Sa.  Oblique inciuence on interface between lossless uielcctries with polar­ ization in thc plane of inciuence.  

7.00 find 7. 100, relating the propagation constants alon g $\mathcal{Y}$ find $\textit{\textbf{z}}$ , fire unchanged.  Therefore the directions of propagation of all the waves remain unaltered.  On this baf'is the situation is as shown in Fig. $7.25a$ .  

At the  point $(z=0,\,y=0)$ ,  the remaining boundary  conditions require  

$$
{\begin{array}{r l r}{\mathrm{E}_{y i}+\mathrm{E}_{y r}=\mathrm{E}_{y t}{\big\vert}}&{}&{{\mathrm{~\textbf~{~II~parallel~to~boundary}}}}\\ {\mathrm{II}_{x i}+\mathrm{II}_{x r}=\mathrm{II}_{x t}{\big\vert}}&{}&{{\mathrm{~\textbf~{~II~parallel~to~boundary}}}}\end{array}}
$$  

In this case, however,  

$$
\begin{array}{r l}&{\mathrm{H}_{x i}=\mathrm{~-~}\Bigg(\frac{\mathrm{F}_{\eta i}}{\cos{\vartheta_{1}}}\Bigg)\frac{1}{\eta_{1}}}\\ &{\mathrm{H}_{x r}=\mathrm{~+~}\Bigg(\frac{\mathrm{F}_{y r}}{\cos{\vartheta_{1}}}\Bigg)\frac{1}{\eta_{1}}\Bigg\}}\\ &{\mathrm{H}_{x t}=\mathrm{~-~}\Bigg(\frac{\mathrm{E}_{y t}}{\cos{\vartheta_{2}}}\Bigg)\frac{1}{\eta_{2}}}\end{array}
$$  

II parallel to boundary  

# So Eqs. 7.106 become  

$$
\left.\begin{array}{l}{\mathrm{E}_{y i}+\mathrm{E}_{y r}=\mathrm{E}_{y t}}\\ {\displaystyle\frac{\mathrm{E}_{y i}-\mathrm{E}_{y r}}{\eta_{1}\cos\vartheta_{1}}=\frac{\mathrm{E}_{y t}}{\eta_{2}\cos\vartheta_{2}}\right]}\end{array}\right\}
$$  

II parallel to boundary  (7. 1 07)  

$$
\frac{\mathrm{E}_{y r}}{\mathrm{E}_{y i}}\equiv\,\bar{\mathrm{I}}_{R}^{~}{}^{\prime}=\frac{Z_{2}{}^{\prime}-Z_{1}{}^{\prime}}{Z_{2}{}^{\prime}+Z_{1}{}^{\prime}}
$$  

$$
\frac{\mathrm{E}_{y t}}{\mathrm{E}_{y i}}\equiv\mathrm{T}^{\prime}=\frac{2{Z_{2}}^{\prime}}{{Z_{2}}^{\prime}+{Z_{1}}^{\prime}}
$$  

$$
\begin{array}{l}{{Z_{1}{'}\equiv\eta_{1}\cos\vartheta_{1}=\displaystyle\frac{-\mathrm{E}_{y i}}{\mathrm{II}_{x i}}=\displaystyle\frac{\mathrm{E}_{y r}}{\mathrm{II}_{x r}}\biggr\}}}\\ {{\mathrm{}}}\\ {{Z_{2}{'}\equiv\eta_{2}\cos\vartheta_{1}=\displaystyle\frac{-\mathrm{E}_{y t}}{\mathrm{II}_{x t}}}}\end{array}
$$  

Conseqllently, this time the propa gation angles enter the impedances $Z^{\prime}$ differently from the way they entered the previolls impc(lances $Z$ . Compare Eqs. 7 . 1 08 and 7 . 1 03, on the one hand , and Eqs. 7. 100 and 7. 1 01 on the other.  In other words : For the same media and angle of incidence, the angles of reflection and refraction arc the same for both polarizations ; so also are the propa gation constants along $y$ and z; but the percentage power reflected (and transmitted) may be radically different in the two cases.  

![](images/2a11813f6d4374619f1be585a0ea6c29677dcc706f3f870562a9bd36f815c561.jpg)  
F i g .  7.2Sb.  Transmission line analogy for the $\scriptstyle\pmb{z}$ dependence and the $\pmb{x}$ and $\pmb{y}$ field components in Fig. $\mathbf{7.25}a$ .  

Unlike any of the cases of normal incidence we have treated, or even of oblique incidence on a perfect conductor, a change of the polariza­ tion of the wave incident obliquely on an interface between two di­ electrics docs much more than merely produce a trivial corresponding chmlgD in  the pobriz:dion  of the l'I:-fJl'cil'd :md tl 111smittl'd  }J": 1·l'S. These matters arc summarized by comparing the transmission-line analogy of Fig. $7.25a$ (which we show in Fig. 7.23b) with that of Fig. 7.23 (shown in Fig. 7.21).  

An interesting example of the different effects produced by the two polarizations arises if we ask for what angle of incidence the reflected wave will vanish : i.e., all the normally directed incident power will be transmitted.  

Taking first Fig. 7.24 $\mathbf{\DeltaE}$ parallel to the boundary), we note that the required condition is a "match" at $z=0$ :  

$$
Z_{1}=Z_{2}
$$  

or  

$$
\eta_{2}\,\cos\,\vartheta_{1p}\,=\,\eta_{1}\,\cos\vartheta_{2p}\qquad\mathrm{~E~parallel~to~boundary}
$$  

where $\vartheta_{1p}$ and $\vartheta_{2p}$ are the particular angles being sought.  Squaring Eq. 7.110 yields  

$$
{\eta_{2}}^{2}(1\,-\,\sin^{2}{\vartheta_{1p}})\,=\,{\eta_{1}}^{2}(1\,-\,\sin^{2}{\vartheta_{2p}})
$$  

which, in the light of Snell's law (Eq. 7. 100), becomes  

$$
\begin{array}{r l r}&{}&{\sin^{2}\vartheta_{1p}=\frac{{\eta_{1}}^{2}-\,{\eta_{2}}^{2}}{{\eta_{1}}^{2}[({v_{2}}/{v_{1}})]^{2}-\,{\eta_{2}}^{2}}}\\ &{}&{=\frac{({\eta_{1}}/{\eta_{2}})^{2}-\,1}{[({\eta_{1}}{v_{2}})/({\eta_{2}}{v_{1}})]^{2}-\,1}}\end{array}
$$  

or  

The angle $\vartheta_{1p}$ is sometimes called Brewstcr's anglc.  As shown by Eq. 7 . 1 1 1a, a real solution for $\vartheta_{1p}$ does not ahmys exist for this polarization. One important situation for which there is no real solution to Eq. 7. 1 1 1a is that in which $\mu_{1}=\mu_{2}$ but $\epsilon_{1}\neq\epsilon_{2}$ '  This is the very common case of two nonmagnetic dielectrics, say, air and glass.  On the other hand, for the very uncommon situation $\epsilon_{1}\,=\,\epsilon_{2},\,\mu_{1}\,\neq\,\mu_{2}.$ , Eq. $7.111a$ becomes  

$$
\sin^{2}\vartheta_{1p}=\frac{1}{(\mu_{1}/\mu_{2})+1}
$$  

or  

which always has a real solution $\vartheta_{1p}<\pi/2!$  

In the second polarization, when $\mathbf{II}$ is parallel to the boundary, Fig. 7.25b shows that a "match" occurs for  

or  

$$
Z_{1}{}^{\prime}=Z_{2}{}^{\prime}
$$  

$$
\eta_{1}\,\cos\vartheta_{1p}{'}\,=\,\eta_{2}\,\cos\vartheta_{2p}{'}
$$  

Squaring Eq. 7. 112 and using Snell's law as before yield  

$$
\sin^{2}\vartheta_{1p}{}^{\prime}=\frac{(\eta_{2}/\eta_{1})^{2}-1}{(\eta_{2}v_{2}/\eta_{1}v_{1})^{2}-1}
$$  

or  

$$
\sin^{2}\vartheta_{1p}{}^{\prime}=\frac{(\mu_{2}\epsilon_{1}/\mu_{1}\epsilon_{2})\r-1}{(\epsilon_{1}/\epsilon_{2})^{2}-1}
$$  

Again, a real Brewster's angle $\vartheta_{1p}{}^{\prime}$ for this polarization docs not always exist; but, as duality ideas suggest, there is now no solution in the uncommon case ,,·hen $\epsilon_{1}\,=\,\epsilon_{2},\,\mu_{1}\,\neq\,\mu_{2},$ , while there is always a solution in the very common case $\mu_{1}\,=\,\mu_{2},\,\epsilon_{1}\,\neq\,\epsilon_{2}$ .  In fact, under this latter condition, Eq. $7.113a$ becomes  

$$
\sin^{2}\vartheta_{1p}{}^{\prime}=\frac{1}{(\epsilon_{1}/\epsilon_{2})+1}
$$  

or  

which is the dual of Eq. 7. 1 1 1b.  

A(l\':mtag;e is taken of the circum:o;bnces described above to produce polarized light.  As we have previously pointed out, ordinary light is not linearly polarized,  but has in;<tea(l (on a  statistical basis) about eCjual amounts of each fundamental linear polarization.  A slab of glass, oriented with re pect to an incident beam of ordinary light so that the  angle of ineidence is $\vartheta_{1p}{}^{\prime}$ ,  \\'ill not reflect any of the light polarized in the plane of incidence.  The reflected \\'[we will then be polnrized entirely parallel to the boundary ; but its intensity may be rather low because the relati\'e dielectric con:;t:lllt of gla:-;s is not very large $\left(\approx\!\cdot\!\1\!-\!\5\right)$ .  ('se  of many sueh slabs ::;t:icked together o\'ercomes thi" difIicul ty, iJe('ause at e:tch interfal'e n  fixed small fraction of the parallel-polarized light i:-; reflected, thereby removing it from the trans­ mitted heam.  Finally, the transmit/cd beam contains the light origi­ nally polarized in the plane of incidence, \\'ith \'( ry l ittle contamination by t he parallel-polarized part.  The latter appear::; almo:-;t entirely in the net reflected \\,:1 \'e ; thus the pile of glase; "labe; c1Tectiyciy separates the unpolarized incident beam into two ::;cparate polarized ones.  It is on :LeCollnt of thi::; applicatioll that Bre\\'loter's angle is more com­ monly knowll as the l)()larizillg a nule.  

7. L3 .;   C lUTI CAL  HEFLECTlO:-.'. \*  ,re  ha\'e seen  that Snell 's  law (Eq, 7 . 1 00b)  doc:; not depen(l upon the polarization,  According to t hie; la\\', whcne\'er $v_{\mathrm{2}}>v_{\mathrm{1}},$ , there exi:-;t large angles of inl·idenC'e $\vartheta_{1}$ for \\'hidl sin $\vartheta_{2}$ would ha\'e to exceed unity.  In other \yonl,.:, if the in­ C'idcnt wa\'e is in :t medium of iil()\\,er light \'Clocity  (larger index of refradion)  than  that  ill  ",hidl  the  transmitted  W:1ye  propagates, nel[s hlw demands  

$$
\sin\vartheta_{2}\geq1
$$  

\\'heneyer  

$$
\sin\vartheta_{1}\geq\frac{v_{1}}{v_{2}}=\sqrt{\frac{\epsilon_{2}\mu_{2}}{\epsilon_{1}\mu_{1}}}
$$  

or  

$$
\vartheta_{1}\,\geq\,\vartheta_{c}\,\equiv\,\sin^{-1}\left(\frac{v_{1}}{v_{2}}\right)
$$  

The an gle $\vartheta_{c}$ is culled the critical a ngle.  

Let us examine firf't the situation of Fig, 7.23  (E paral lel to the boundary) as $\vartheta_{1}\longrightarrow\vartheta_{c}$ when $v_{2}>v_{1}$ .  ,Ye note from ilJ(' condition $v_{2}>v_{1}$ that in Snell 's law $\vartheta_{2}>\vartheta_{1}$ for $\vartheta_{1}<\vartheta_{c}$ ; hellee the direction of propagation of the transmitted wave in this case actually makes a larger angle \\'ith the $+z$ -axis than docs that of the incident wave.  The refraction bends  the wave away from the normaL  ,\'hen $\vartheta_{1}\,=\,\vartheta_{c;}$ , sin $\vartheta_{2}=1$ and $\vartheta_{2}=90^{\circ}$ .  The transmitted wave is then propagating entirely parallel to the boundary, so we would expect that $\mathrm{II}_{y t}=0$ . Sinc'e cos $90^{\circ}=0_{:}$ , Fig. 7.2 t 8hm\"l', that $Z_{2}=\infty$ and that the incident and reflected eledric fields must be eqllal (see also Err, $7.103a)$ .  "Ire ha\'e a cOl ldition of "total reflection" in \\'hich the p O\\'er reflected back into medium  1  equals that incident in medium 1 .   The real po\\"er transmitted in a normnl direction into medium 2 (i.e., along $+z)$ is zero, n!though there is a field in medium 2 representing a uniform plnne \\"aye tra\'eling along the $-y$ -nxis. $\Lambda s$ such, this field does not "ary \\'ilh $\textit{\textbf{z}}$ nt all.  

What must happen physirally i f  \\'e 11m\' make $\vartheta_{1}>\vartheta_{c}\colon$ ?  

First, there must be sOllie field i n  medium 2 ;  for, i f  not, med ium 2 woulel sud cIPnly be aeiing j ust like a Jwrfeet conductor, merely ber;tuse \\"e ha ppened to C'hoose f;ome f'peci:d :\llgles of incidence in medium 1 . This i s  uJll'ensonable.  Be:-idcs, \\'e should be remindec] of the experi­ mental faet in optiC's that, if a prism is causing an internal rritieal re­ f1ertion ,  alll] anot her f'im i la r  one is pressed c1 o"c1y aga inf't one of t he sides at \dlich the cri ti cal refkdion is oC('lIlTi n g, most of the light goes i n t o  the H colld prism inst ead of bci ng cri t ically rcfleded !  There must ha\'e been some field j ust oll/liide the original prism sl\l'face ; ot hen\'ise, ho\\" could hringing lip the second pri"m (':Ulse any ('h:lnge '?  

G rant ed that t here is sO lli e field in medium 2, theil, it mUf;t be such that no real (t ime-a\'erage) pm\'('r f1 m",; i n  the $+z$ diredion as lon g as $\vartheta_{1}\geq\vartheta_{c}$ •  This requiremcnt stems f!"Om the ,,'ell-kno\\'n experimental fact in optiC's that "total reflection" occurs for all angles of incidence greater than the cri t ic-al angle,  

Thirdly, with referellC'c to Fig. 7,23, there is still the problem of in­ sur i n g  that the im'ident,  refleeied,  and  t r:tnf;mitted waves stay  "in :-tcp" along the $y$ direetion.  For the reflected w:n-e, this condition is easily met if $\vartheta_{r}\,=\,\vartheta_{i}$ as usual.  For the refracted W:l\'e, ho\\'ever, the present situation $\vartheta_{1}>\vartheta_{c}$ makes Snell's law demand $\left(\upsilon_{1}/{\sin\vartheta_{1}}\right)<\upsilon_{2},$ , or $\beta_{01}$ sin $\vartheta_{1}>\beta_{02}$ '  But the mwe in med ium 2 must ha\'e an dTeC'ti\'e phfl e eonstant alona $y$ \\'hieh efjlwls $\beta_{01}$ sin $\vartheta_{1}$ , and \\'e see tklt this is grca/er than that $\left(\beta_{02}\right)$ of any possible 1tnljonn plane lcaec in medium 2 !  

Finally, since the incident \\"ave is $x^{\star}$ -pobrized, i t  should he possible t o  meet the houndary conditions with reflected and transmitted waves, both also $x^{\cdot}$ -polarized.  

The conelusioll is almost inescapable : The W[LYe in medium 2 must be a nonwujonn plane teat'e, arranged to attenuate in the $+z$ direction (boundary condition at infinity), Imye a phase delay along $-y$ with a pha"e ron:-tant $\beta_{2}=\,+\sqrt{{\beta_{02}}^{2}+\alpha^{2}}>\,\beta_{12}$ , and to be TE "'ith respect to the $y$ (or z) directions, $\Lambda$ sketch of the conditions a ppears in Fig. 7.2G.  

![](images/db47e67760b4ff1135f4c766a3e874b3a1460885f5d1fed0ddf7c84b4089ef18.jpg)  
Fig. 7.26.  ObJique incidence beyond the critical angle on  an interface between loss)ess dielectrics $(\epsilon_{1}\mu_{1}>\epsilon_{2}\mu_{2})$ '  Drawn either for polarization in the plane of in­ cidence, or paralic) to the interface.  

Analytically, referring to the foregoing discussion and to Eqs. 7.54, this field must be of the TE form :  

$$
\begin{array}{r l r}&{}&{\bar{\mathfrak{Y}}_{2}=-a_{\iota}j\beta_{2}+a_{z}\alpha_{2}\qquad\alpha_{2},\beta_{2}>0\qquad\beta_{2}{}^{2}-\alpha_{2}{}^{2}=\beta_{02}{}^{2}}\\ &{}&{\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad(}\\ &{}&{\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\quad}\end{array}
$$  

$$
\mathbf{II}_{t}=\frac{\bar{\mathbf{\nabla}}\times\mathbf{\deltaE}_{t}}{j\omega\mu_{2}}=\left(\frac{a_{y}\alpha_{2}+a_{z}j\beta_{2}}{j\omega\mu_{2}}\right)\mathrm{E}_{x t}e^{j\beta_{2}y}e^{-\alpha_{2}z}
$$  

The requirement of phase match along the boundary becomes  

$$
\beta_{2}\,=\,\beta_{01}\,\sin\vartheta_{1}
$$  

and therefore on account of Eqs. 7.1 1Ga and 7.1 15  

$$
\alpha_{2}=+\sqrt{{\beta_{01}}^{2}\sin^{2}\vartheta_{1}-{\beta_{02}}^{2}}=+{\beta_{01}}\sqrt{\sin^{2}\vartheta_{1}-\sin^{2}\vartheta_{\sigma}}
$$  

With regard to the remaining boundary conditions on the tangential fields, ,ye may still apply Eqs. 7.101 and $7.102a$ .  For Eq. 7.102b, how. ever, matters are altered slightly because, whereas  

$$
\frac{\mathrm{E}_{x i}}{\mathrm{H}_{y i}}=\mathrm{-\,}\frac{\mathrm{E}_{x r}}{\mathrm{H}_{y r}}=\frac{\eta_{1}}{\cos\vartheta_{1}}=Z_{1}\mathrm{~=~real~}
$$  

88 before, we now find from Eqs. 7.116b, 7.11&, 7.117b, and 7.115  

$$
\mathrm{Z}_{2}\equiv\frac{\mathrm{E}_{x t}}{\mathrm{H}_{y t}}=\frac{\dot{\gamma}\omega\mu_{2}}{\alpha_{2}}=\frac{\dot{\jmath}\omega\mu_{2}}{\beta_{01}\sqrt{\sin^{2}\vartheta_{1}-\sin^{2}\vartheta_{0}}}
$$  

$$
\frac{j_{\eta_{2}}}{\sqrt{(\sin\vartheta_{1}/\sin\vartheta_{e})^{2}-1}}=j X_{2}
$$  

which is positive imagjnary (inductive) and independent of frequency. Consequently the/arm of Eqs. 7.103 remains unchanged, but the values in it are rather different:  

$$
{\frac{\mathbf{E}_{x r}}{\mathbf{E}_{x i}}}={\hat{\Gamma}}_{R}={\frac{\mathbf{Z}_{2}-Z_{1}}{\mathbf{Z}_{2}+Z_{1}}}={\frac{j X_{2}-Z_{1}}{j X_{2}+Z_{1}}}=e^{j\psi}
$$  

$$
{\frac{\mathbf{E}_{x t}}{\mathbf{E}_{x i}}}\equiv\mathbf{T}={\frac{2\mathbf{Z}_{2}}{\mathbf{Z}_{2}+Z_{1}}}={\frac{2j X_{2}}{Z_{1}+j X_{2}}}
$$  

where  

$$
\psi\,=\,2\,\tan^{-1}\left({\frac{Z_{1}}{X_{2}}}\right)\qquad0\leq\tan^{-1}\left({\frac{Z_{1}}{X_{2}}}\right)\leq{\frac{\pi}{2}}
$$  

The boundary condition results just found arc partially summarized in Fig. $7.27a$ , ,,-hich represents them i n  the form of the equivalent tran ­ mission line appropriate to the $z_{\mathrm{:}}$ -axis features of the problem.  Note that medium 2 presents a losslcss (inductive) 10:.Ld to the line of medium  

![](images/42f49305cc38e3ec2680279ea3572ba8d2c209e4a5ced550f7abac51a9cda425.jpg)  

F i g .  7.27.  Transmission-line ann,logies for z dependence  and $_x$ and $_y$ field com­ ponents in Fig. 7.20 ; $(a)$ with pol:J,rizatiun Imrallel to interface, and $(b)$ with polariza­ tion in the plane of incidence.  

1 in this casc, which accounts propcrly for the abscncc of real power cntering medium 2 in thc $^z$ dircction.  Thi:> is, of cour"e, chcckcd hy thc fact that $\vert\;\bar{\Gamma}_{\!R}\vert=1$ in Eq. $7.119a$ .  l\ gain, one must not lo!-'c "ight of thc fact that tra,"eling-waye propagation is takin g  place along thc $-y$ dircction on both "ides of the boundary, and that timc-u,"crage powcr is flo,,"ing accordingly along $-y$ in both mcdia.  

In the casc of polarization in the plane of incidenec, bcyond critical anglc (Figs. $7.25a$ and 7.2G) , the magnctic field will h 1\'e only an $x$ componcnt.  The t ran;;mitted nonuniform planc '\"ave  in  mcdium 2 will bc of thc 'I'M type (Eqs. 7.53) ,  

$$
\begin{array}{r l}&{\bar{\mathbf{\nabla}}_{2}\,=\,-\,a_{y}j\beta_{2}+\,a_{z}\alpha_{2}\qquad\alpha_{2},\,\beta_{2}>0\qquad\beta_{2}^{2}-\,{\alpha_{2}}^{2}\,=\,{\beta_{02}}^{2}}\\ &{{\bf I I}_{t}\,=\,a_{x}\mathrm{II}_{x t}e^{j\beta_{2}y}e^{-\alpha_{2}z}\qquad\qquad\qquad\qquad\qquad\qquad\quad}\\ &{{\bf E}_{t}\,=\,-\,\frac{\overbar{\mathbf{\nabla}}^{\times}\mathbf{\nabla}\mathbf{\times}\,\mathrm{II}_{t}}{j\omega\epsilon_{2}}=\frac{-\,(a_{y}\alpha_{2}+\,a_{z}j\beta_{2})}{j\omega\epsilon_{2}}\,\mathrm{II}_{x t}e^{j\beta_{2}y}e^{-\alpha_{2}z}\quad}\end{array}
$$  

with Eqs. $7.117a$ and 7. 1 17b remaining unchangcd.  Abo as befm·c  

$$
{\frac{-\mathrm{E}_{y i}}{\mathrm{II}_{x i}}}={\frac{\mathrm{E}_{y r}}{\mathrm{II}_{x r}}}\equiv Z_{1}^{\,\prime}\,=\,\eta_{1}\,\cos\,\vartheta_{1}\,=\,\mathrm{rcal}
$$  

but now  

$$
{\frac{-\mathrm{E}_{y t}}{\mathrm{H}_{x t}}}\equiv\mathrm{Z}_{2}\prime={\frac{\alpha_{2}}{j\omega\epsilon_{2}}}=\,-j\eta_{2}\,\sqrt{\left({\frac{\sin\vartheta_{1}}{\sin\vartheta_{c}}}\right)^{2}-1}\,=\,-j X_{2}\prime
$$  

which is ncgative imaginary (capacitive) and indcpendcnt of frequcncy. Thus  

$$
\frac{\mathrm{E}_{y r}}{\mathrm{E}_{y i}}\equiv\bar{\mathrm{I}}_{R}{'}=\frac{\mathrm{Z}_{2}{'}-\mathrm{Z}_{1}{'}}{\mathrm{Z}_{2}{'}+\mathrm{Z}_{1}{'}}=\frac{-\mathrm{Z}_{1}{'}-j\mathrm{X}_{2}{'}}{\mathrm{Z}_{1}{'}-j\mathrm{X}_{2}{'}}=e^{j\psi}
$$  

$$
\frac{\mathrm{E}_{y t}}{\mathrm{E}_{y\it{i}}}\equiv\mathrm{^{\prime}{I^{\prime}}}=\frac{2\mathrm{Z}_{2}\mathrm{^{\prime}}}{\mathrm{Z}_{2}\mathrm{^{\prime}}+\mathrm{Z}_{1}\mathrm{^{\prime}}}=\frac{-2j\mathrm{X}_{2}\mathrm{^{\prime}}}{\mathrm{Z}_{1}\mathrm{^{\prime}}-j\mathrm{X}_{2}\mathrm{^{\prime}}}
$$  

In thi  case, however, we must put  

$$
\psi^{\prime}=\mathrm{\-2\tan^{-1}}\left({\frac{Z_{1}{}^{\prime}}{X_{2}{}^{\prime}}}\right)\qquad0\leq\tan^{-1}\left({\frac{Z_{1}{}^{\prime}}{X_{2}{}^{\prime}}}\right)\leq{\frac{\pi}{2}}
$$  

which should be compared carefully with Eq. 7.120, recog:1.izing that by our definitions $\mathbf{Z_{1}},X_{2},Z_{1}^{\prime}$ , and $\pmb{X_{2}}^{\prime}$ are all p08itive real number8. Figure 7.27b summarizes the conditions leading to Eqs. 7. 123 and 7.124.  

We have now seen for the first time a physical situation giving rise to nonuniform plane waves.  They occur here as the refracted wave "on the other :;;ide of a reflection J,eyolHl critic'al angle," when the incident and reflccte(l wayes ar c  both wujo7'ln plane waycs !  This heing thc case, howcver, one may wonder whether 01' not the bmden of shifting the refraded waye from a uniform t o  a llomlll iform plane \\"tn'e, as the an gle of i ncidellce  pa:;; es  smoothly from zero to  "allies heyond the critic-al angle $\vartheta_{\mathfrak{c}_{\mathrm{i}}}$ ) must ahmys he hand led as a brand-new problem­ completely independent of the :,;olution for $\vartheta_{1}\,\le\,\vartheta_{c}$ •  

The a nswer is that the idea  of a cOlllple.r anylc oj refraction, $\bar{\vartheta}_{\cdot2}=$ $\vartheta_{2R}+j\vartheta_{2I}$ , call he u ed t o  make the transiti oll in an almo;;t C'ompletcly automatic  manncr.  As an  example,  take  the  case of polarization parallel to the boundary (Fig. 7.23 ) .  

":hen $\vartheta_{1}<\vartheta_{c},$ , or, indeed, bcfore we had any particular reason to expect a "critical angle" prohlem at all, we wOllld have said that the transmitted \\'ave must J JC given by u wujol'llt plane wave exprctitiion similar to Eq. 7.SG.  Speci fically,  

(u) Et = auBrte-jpoz cos D2e+jPozvsind2  

$$
\mathbf{II}_{t}=\frac{\mathrm{F}_{x t}}{\eta_{2}}\,(u_{y}\,\cos\vartheta_{2}+u_{z}\,\sin\vartheta_{2})e^{-j\beta_{02}z\cos\vartheta_{2}}e^{+j\beta_{02}y\sin\vartheta_{2}}
$$  

with Eqs. 7. 100, 7. 103, ::mcl 7. 101 used to meet the boundary conditions.  

When it came to evaluation of $\vartheta_{2}$ , however, we might discover that in Snell's law  

$$
\sin\vartheta_{2}=\left({\frac{v_{2}}{v_{1}}}\right)\sin\vartheta_{1}={\mathrm{real~and}}>1
$$  

because $v_{2}>v_{1}$ and $\vartheta_{1}$ was rather large.  In that case, let $\vartheta_{2}$ be com­ plex, and find out what it must be to satisfy Snell's law anyway !  Ac­ cordingly,  

$$
\begin{array}{c}{{\sin{\bar{\vartheta}_{2}}=\sin{\vartheta_{2R}}\cosh{\vartheta_{2I}}+j\cos{\vartheta_{2R}}\sinh{\vartheta_{2I}}}}\\ {{=\displaystyle\left(\frac{v_{2}}{v_{1}}\right)\sin{\vartheta_{1}}=\mathrm{real\;and}>1}}\end{array}
$$  

Therefore the only possibility is  

$$
\cos\vartheta_{2R}=0\qquad\vartheta_{2R}=\frac{\pi}{2}
$$  

to make  

$$
\sin\,{\bar{\vartheta}_{2}}\,=\,+\cosh\vartheta_{2I}\,=\,\biggl(\frac{v_{2}}{v_{1}}\biggr)\sin\,\vartheta_{1}\,=\,\mathrm{real~and}\,>1
$$  

This defines $\vartheta_{2I}$ , except for  algebraic  sign ; $\vartheta_{2I}\,=\,\pm\cosh^{-1}\left[(v_{2}/v_{1})\right]$ sin $\vartheta_{1}]$ .  Consequently,  

$$
\bar{\vartheta}_{2}\,=\,\cos\vartheta_{2R}\,\cosh\vartheta_{2I}\,-\,{j}\,\sin\vartheta_{2R}\,\sinh\vartheta_{2I}\,=\,-j\sinh\vartheta_{2I}
$$  

# 3 6 8   ElECTROMAGNETIC ENERGY TRANSMISSIO N  AND RADIATIO N  

Employing the above values for sin $\bar{\vartheta}_{2}$ and cos $\bar{\vartheta}_{2}$ in the transmittcd­ ficld exprcssions, and using Sncll's law, $\beta_{02}\,\sin\,\bar{\vartheta}_{2}=\,\beta_{01}\,\sin\,\vartheta_{1},$ in the exponents, we find  

$$
\mathrm{II}_{t}=\frac{\mathrm{E}_{x t}}{\eta_{2}}\,(-a_{y}j\sinh\vartheta_{2I}+a_{z}\cosh\vartheta_{2I})e^{j\beta_{01}y\sin\vartheta_{1}}e^{-\beta_{02}z\sinh\vartheta_{2I}}
$$  

Now it is reasonable to assumc that the solution ,,·c want must die out rather than become infinite as $z\rightarrow+\infty$ ; at least this is thc only boundary condition at infinity \\"hich is consistent "'ith our previous assumptions about the incident wave being the only source in the problem.  Thus we may write  

$$
\begin{array}{l}{{\alpha_{2}\,=\,\beta_{02}\,\sinh\,\vartheta_{2I}>0\qquad\qquad\vartheta_{2I}>0}}\\ {{\qquad\beta_{2}\,=\,\beta_{01}\,\sin\,\vartheta_{1}\,=\,\beta_{02}\cosh\,\vartheta_{2I}}}\end{array}
$$  

so that  

$$
\frac{\cosh\vartheta_{2I}}{\eta_{2}}=\frac{\beta_{2}}{\beta_{02}\eta_{2}}=\frac{\beta_{2}}{\omega\mu_{2}}
$$  

and  

$$
\frac{-j\sinh\vartheta_{2I}}{\eta_{2}}=\frac{-j\alpha_{2}}{\beta_{02}\eta_{2}}=\frac{\alpha_{2}}{j\omega\mu_{2}}
$$  

"\Ve can thcrefore convert the last field expressions to  

$$
\begin{array}{r l r}&{}&{\mathbf{E}_{t}=a_{x}\mathrm{E}_{x t}e^{j\beta_{2}y}e^{-\alpha_{2}z}\,\,\,}\\ &{}&\\ &{}&{\mathbf{II}_{t}=\left(\frac{a_{y}\alpha_{2}+a_{z}j\beta_{2}}{j\omega\mu_{2}}\right)\mathrm{E}_{x t}e^{j\beta_{2}y}e^{-\alpha_{2}z}\,\,\,}\\ &{}&{\beta_{2}{}^{2}-\left.\alpha_{2}{}^{2}=\beta_{02}{}^{2}\right.\,\,\,}\\ &{}&{\beta_{2}=\beta_{01}\sin\vartheta_{1}\,\,\,\,}\end{array}
$$  

which agrees precisely with Eqs. 7. 11G and 7. 1 17.  

Thc straightforward usc of a complex angle of refraction in Snell's law, plus the election of $\footnote{I n t h i s p a p e r,w e h a v e a s s u m e d p e r f e c t C S I t o i n v e s t i g a t e t h e b e s t a c h i e v a b l e p e r f o r m a n c e.T h e p e r f o r m a n c e u n d e r i m p e r f e c t C S I i s w o r t h f u r t h e r i n v e s t i g a t i o n b y r e f e r i n g t o e x i s t i n g a n a l y t i c a l w o r k s~.}$ choice regarding the behavior of the refracted 30lution at infinity, allows us to carry the refracted fielel solution con­ tinuously through from uniform to nonuniform plane waves as the incident anglc $\vartheta_{1}$ passes through the critical value $\vartheta_{c}$ •  

One of thc roles of thc nonuniform planc wave in a lossless mcdium may bc summarized from the examples just treateel.  It arises when bounelary  conelitions  require  an effective phase  velocity  (or  wave length) in some space direction which is less than that provieleel at the given frequency by the  conventional  "free  space"  phase velocity $\breve{1}/\sqrt{\epsilon\mu}$ [or wave  length $2\pi/(\omega\sqrt{\epsilon\mu})]$ in  the  surrounding medium. Larger phaf'e velocities (or wave lengths) in a given direction can be achieved with uniform plane waves at real oblique angles of propaga­ tion ; smaller ones, however, require "uniform" plane waves at complex angles of propagation-which is to say, actually, nonuniform plane waves oriented to provide large space-rates-of-change of phase along the direction in question.  The price of such small wave lengths (or rapid phase changes) along one direction, however, is complete attcnua­ tion in another (perpendicular) direction.  Compressing phase velocity along one axis loses amplitude at right angles !  

These matters are illustrated even more forcefully in the following examples of guided waves.  

# 7.5  Guided Waves \*  

In studying the oblique incidence of uniform plane waves upon plane boundaries, we have so far stressed primarily the beh:wior of the fields as regards the direction normal to the boundary.  Examination of these problems from the point of view of the direction parallel to the bound­ ary instead leads to the concept of guided waves.  This approach is by no means the only one for introducing guided waves, but it does furnish one illuminating view of the problem.  

# 7.5. 1  Metallic (Rectangular) Wave Guides \*  

Consider the problem of an $_x$ -polarized uniform plane wave at an oblique angle of incidence $\vartheta$ upon a perfect conductor (Fig. 7.21) . The total field is given in Eq. 7.fJ7.  

This field has the property that $\mathrm{E}_{x}=0$ , not only on the plane $\boldsymbol{z}=0$ but also on the planes  

$$
z_{m}=\frac{-m\lambda}{2\cos{\vartheta}}=\frac{-m\lambda_{z}}{2}\qquad\quad m\,=\,1,\,2,\,\cdots
$$  

Thus it \"ill still be a solution both to l\faxwell's equations and the boundary conditions if a second perfect conductor is inserted at the position $z_{m}=-a_{:}$ , with  

$$
a\,=\frac{m\lambda}{2\,\cos\,\vartheta}=\frac{m\lambda_{z}}{2}\,\qquad m\,=\,1,\,2,\,\cdots
$$  

Under  these  conditions,  the  tangential  electric  field $\left(\mathrm{E}_{\pm}\right)$ vanishes  

![](images/0c6d5db3e8ea449e09d0fc61912dd1246727f9bd0ab79350adaaa936a0d48507.jpg)  
Fig. 7.28 .  Construction of a rcct an u1ar wavc-gui,]e solut ion from the obliquely ineident and n,fl"d('d wav('s for a mct :d plane $z\,=\,0$ . $(a)$ Addit ion of  idc w:t1I, $z\,=\,-a\,=\,-\,(m\lambda_{z}/2)\,;\,(b)$ ) addition of top and hott om wal l", $\boldsymbol{z}\,=\,\boldsymbol{0}$ :tIl(1 $x=b<a$ .  

automatically on the surface of both conductors.  Consequently, as sho\\'n schematically in  Fig. $7.28a$ , the  field  

$$
\begin{array}{l}{{{\bf{E}}=[\,-a_{x}2j\mathrm{{E}}\sin\,(\beta_{0}z\,\cos\vartheta)]e^{j\beta_{0}\gamma\sin\vartheta}}}\\ {{\mathrm{}}}\\ {{{\bf{I I}}=\displaystyle\frac{2E}{\eta}\left[a_{y}\cos\vartheta\,\cos\,\left(\beta_{0}z\,\cos\vartheta\right)\right.}}\\ {{\qquad\qquad\left.-a_{z}j\sin\vartheta\,\sin\,\left(\beta_{0}z\,\cos\vartheta\right)\right]e^{j\beta_{0}\gamma\sin\vartheta}}}\end{array}
$$  

is a solution in t.he space regi on $(-a\leq z\leq0;\,-\infty<y<+\infty)$ , pro­ vided Eq. 7.12G is met.  ::'. Ioreo\"er, this solution constitutes $^\mathrm{a}$ traveling wave in the $-y$ direction, completely confined in the $^z$ dircction.  The "source" for it must now be regarded as located at $y=+\infty$ .  

Evidently, t\\'o more perfectly conductin g  planes might j ust as \\'ell be added to the system, one at $x\,=\,0$ and the other at $x=b<a;$ , as shown in Fig. 7.28b.  Since these planes are perpendicular to the only component of the electric field $(\mathrm{{F}}_{x})$ , they do not require any modifica­ tion of the field solution to meet their boundary conditions.!  

We now have a tntyeling \\,:1.ve along $-y$ , completely confined in a hollow recbngular pipe definell by $0\le x\le b$ and $-a\le z\le0$ (Fig. 7.28b).  The structure is serving as a wave guide.  It is of interest, then,  

! It is worth while to pause here an,l consi(ler whether this whole scheme would work if one were to start wi th the magnetic instead of the electric field along $\pmb{\sigma}$ . to ask how the propagation of this ,mve in the "'ave guide varies with frequency, assuming dimensions $^{\footnote{I n t h i s p a p e r,w e h a v e a p e r,w e h a v e a s s u m e a r e a r i m p i c a t i o n s c e,w e h a v e a s s u m e a r e a r e a r t h e c o m p e r f o r m a n c e.T h e p o r m a n c e u n d e r i m p e r f e c t i o n s a n d w a r e a r e a r e a r e a r e a r m o n s h i p s o f$ and $\boldsymbol{b}$ arc fixed.  In view  of Eq. 7. 12G, $\vartheta$ now becomes merely a parameter, fixed by the vallie of $^{\footnote{a n t h i s p a p e r,w e h a v e a s s u m e a s s i n g a u t h o r.T e l:~+86-1088236256.E-m a i l a d d r e s s:t a n c e,w e a n c e a n g l i c a l i n s a n d d e l a t o m a n i n g.}$ and the free-space (not va cuum) wave length $\lambda$ .  The latter is really j ust n, measure of the frequen('y, giyen the values E and $\mu$ of the medium which fills the guide, because by definition  

$$
\uplambda\equiv\frac{2\pi}{\beta_{0}}\equiv\frac{2\pi}{\omega\sqrt{\epsilon\mu}}\overline{{{\upmu}}}\,
$$  

Thus we shall wish to eliminate $\vartheta$ ill some of our immediate discus ioll.  

The important questions about thi  w n'e arc :  ( 1 )  How docs  the $\mathcal{Y}$ yariation depend on $\omega$ (or A) '?  (2)  I row docs the flow of complex power alon g $-y$ depend upon frequency ?  (3) l I o\\' docs the field dis­ tribution a('ro s t1:e tr:lllsY(;rse dimensions $(x,z)$ ,'ar)' ,,·ith frequency ?  

First,  "'e define the  gllide 1C0 1'C  length $\lambda_{g}$ as the distame beb\'een equiphase surfaces measurel\ along the guide propagation axis $(-y$ in this case) .  Previously we called this $\lambda_{y},$ so  

$$
\uplambda_{g}\equiv\uplambda_{y}=\frac{\uplambda}{\sin\vartheta}
$$  

But in view of Err. 7 . 1 2G  

$$
\sin\vartheta\,=\,\sqrt{1\,-\,\cos^{2}\vartheta}\,=\,\sqrt{1\,-\,\biggl(\frac{\lambda}{2a\overline{{{/m}}}}\biggr)^{2}}
$$  

and Eq. 7 . 1 20 be(;omes  

$$
\lambda_{g}=\frac{\lambda}{\sqrt{1~-~(\lambda/\lambda_{m,0})^{2}}}>\lambda\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\mathrm{for}\,\lambda\,\le\,\lambda_{m,0}
$$  

where  

$$
\lambda_{m,0}\equiv{\frac{2a}{m}}
$$  

Then using Eqs. 7. L2G ami 7. 1 20 to eliminate $\vartheta$ from the field ex­ pressions (Eqs. 7. 127), ami defining  

$$
\beta_{g}\equiv|\,\beta_{y}|\equiv{\frac{2\pi}{\lambda_{g}}}=\beta_{0}\sin\vartheta
$$  

we find  

$$
\begin{array}{l}{{\displaystyle{\bf E}=\mathrm{}-\left[a_{x}2j\mathrm{E}\sin\left(\frac{m\pi z}{a}\right)\right]e^{j\beta_{y}y}\qquad,\quad m\,=\,1,\,2,\,3,\,\cdots\,}}\\ {{\displaystyle{\bf H}=\frac{2E}\eta\left[a_{y}\left(\frac{\lambda}{\lambda_{m,0}}\right)\cos\left(\frac{m\pi z}{a}\right)\right.}}\\ {{\displaystyle{\bf\qquad\quad}-a_{z}j\left(\frac{\lambda}{\lambda_{g}}\right)\sin\left(\frac{m\pi z}{a}\right)\right]e^{j\beta_{y}y}\qquad,\quad m\,=\,1,\,2,\,3,\,\cdots\,}}\end{array}
$$  

It is clear from Eq. 7. 134 that the behavior of the fields as a function of the transyerse coordinates $\left(x,z\right)$ does not depend upon frequency. There is actually no $x$ depemlence, and the $\textit{\textbf{z}}$ dependence is sinusoidal with dimension $^{a}$ , an integer number $\left(m\right)$ of half-periods.  The wave is TE with respect to the guide $(y)$ axis, having an electric field linearly polarized in the transverse plane (along $x$ ) and both a transverse (z) component amI a longitudinal $(y)$ component of magnetic field.  

On account of their m half-period variations along the wide dimension $^{a}$ , and their zero variation along the narrow dimension $\upsilon$ , these rec­ tangular "'aYe-guide field solutions are called $\Gamma\mathrm{F}_{m,0}$ waves or modes. They are different for different (arbitrary) integer choices of $m$ , so we actually have an infinite set of solutions for a given guide size and a specified frequency.  Nevertheless,  the transyerse variation of the fields depends only on m, and not on frequency, so we can easily identify one solution by its m value and then consider its behavior as a function of frequency.  Each of the "modes" $\mathrm{TE}_{1,0}$ , $\mathrm{TE}_{2,0},\,\cdot\cdot\cdot,\,\mathrm{TE}_{m,0}$ may be regarded as a separate rectangular wave-guide solution which varies in its own way with frequency.  

To study the frequency variation of a $\mathrm{TE}_{m,0}$ mode, refer first to Eqs. 7.131 and 7. 132.  At very high frequencies, $\lambda\to0$ and $\lambda_{g}\longrightarrow\lambda$ $\to\,0.$ .  As the frequency is lowered, however, $\lambda\longrightarrow\lambda_{m,0}$ amI $\lambda_{g}\,\rightarrow\,\infty$ . When $\lambda>\lambda_{m,0}$ , on the other hand, $\lambda_{g}$ must become imaginary  

$$
\lambda_{g}=\frac{\iota_{-)}^{+}\lambda}{\sqrt{(\lambda/\lambda_{m,0})^{2}-1}}\qquad\mathrm{~for~}\lambda>\lambda_{m,0}
$$  

The meaning of Eq. 7.135 stems from Eq. 7.134, where  

$$
\begin{array}{c}{{e^{j\beta_{\theta}y}=e^{j(2\pi y/\lambda_{\varepsilon})}=e^{(\frac{+}{-})^{\frac{\dag}{\left(\left(2\pi/\lambda\right)\left(\sqrt{\lambda_{m,0})^{2}-1}\right)}\left|y\right\rangle}}}}\\ {{=e^{(\frac{+}{-})\alpha_{g}y}\qquad\quad\mathrm{for}\;\lambda>\lambda_{m,0}}}\end{array}
$$  

shm"s pure attenuation along $(\bar{+})\;\,\mathcal{Y}$ !   Actually \ye would choose the $+$ sign in Eqs. 7. 135 and 7.13G, since we are discussing the problem for a source at $y=+\infty$ .  The solution should therefore vanish (rather than grow exponentially) as $y\to-\infty$ , and grow (rather than vanish) at $y=+\infty$ .  

At long wave lengths (low frequencies) , the uniform plane waves from \yhich \ye originally constructed the wave guide solution have changed into nonuniform plane \\"aYeS.  This assertion is confirmed from Eqs. 7. 126 and 7. 132 by the fact that cos $\vartheta>1$ when $\lambda>\lambda_{m,0.}$ , and sin $\vartheta$ is pure imaginary in Eq. 7. 130.  The angle $\vartheta$ becomes complex, $\Bar{\pmb{\vartheta}}\,=$ $\pi+j\vartheta_{I}$ (o $\mathrm{~r~}\boldsymbol{\bar{\vartheta}}\,=\,-j\vartheta_{I}\rangle$ .  We expect no real (time-average) power flow down the guide under these conditions and, of course, we never expected any in directions normal to each of the four perfectly conducting walls .  Let us check these features of the power flow by examining the ,yave impedances.  

Observe from Eq. 7.134 that  

$$
\begin{array}{l}{{\mathrm{Z}_{-y}\equiv\frac{\mathrm{E}_{x}}{\mathrm{H}_{z}}=\,\eta\left(\frac{\uplambda_{g}}{\uplambda}\right)}}\\ {{\mathrm{\LambdaZ}_{z}\equiv\frac{\mathrm{E}_{x}}{\mathrm{H}_{y}}=\,-j\eta\left(\frac{\uplambda_{m},0}{\uplambda}\right)\tan\left(\frac{m\pi z}{a}\right)}}\end{array}
$$  

Accordingly, since $\mathbf{Z}_{z}$ is always pure imaginary, there is only reactive power flowing in the $\pm z$ directions at all frequencies. $\mathbf{Z}_{-y}$ however is positive real when $\lambda<\lambda_{m,0}$ and becomes pure imaginary (inductive) "'hen $\lambda>\lambda_{m,0}$ $\uplambda_{g}$ becomes positive imaginary).  Real power does flow down the guide at high frequencies $(\uplambda<\uplambda_{m,0})$ , but only (inductive) reactive po,,'er flows at low frequencies $(\uplambda>\uplambda_{m,0})$ '  Thus the wa,'e guide acts like a high-pass filter, with a cUlo.f! frequency $\omega_{m,0}$ defined by  

$$
\omega_{m,0}=\frac{2\pi}{\uplambda_{m,0}\sqrt{\epsilon\mu}}=\frac{\pi m}{a\sqrt{\epsilon\mu}}
$$  

The mechanism of propagation $(\uplambda<\uplambda_{m,0})$ down the guide can be represented in terms of uniform plane ,\'aves by the familiar optical type of ray-tracing picture of a single unit-field-strength ray alternately reflected from each side wall , as in Fig. $7.28a$ , in \yhich ,,'e focus at­ tention only on the space between $z=0$ and $z=-a$ ; or, more sym­ metrically, by considering two sets of multiply reflected mys, each of half field strength, shown in the similar picture Fig. $7.29a$ .  Alterna­ tively, if we mentally remove the side walls at $z=0$ and $z=-a$ , the interference pattern in all space of just two rays ,  each of unit field strength, as shown in Fig. $7.29\time10$ , ,yill produce tangential electric field nodal planes (dotted lines) where the walls used to be (and also at other such planes spaced $\acute{\iota}_{2}\uplambda_{z}$ from these) .  

In either view, regarding the dimension $^{\footnote{I n t h i s p a p e r,w e h a v e a s s u m e d p e r f e c t C S I t o i n v e s t i g a t e t h e b e s t a c h i e v a b l e p e r f o r m a n c e.T h e p e r f o r m a n c e u n d e r i m p e r f e c t C S I i s w o r t h f u r t h e r i n v e s t i g a t i o n b y r e f e r i n g t o e x i s t i n g a n a l y t i c a l w o r k s~.}$ and mode index $^{m}$ as fixed, ,ye may use Eqs. 7.120 and 7. 132 to determine $\vartheta$ as a function of fre­ quency for the mth mode field.  

$$
\cos\ i\quad\frac{\lambda}{\uplambda_{m,0}}
$$  

As long as $\lambda<\lambda_{m,0}$ , $a>m\uplambda/2$ from Eq. 7.120, and, according to Eq. 7.129 or 7.13 1 , $\uplambda_{z}>\uplambda$ .  This condition can always be met with a real angle $\vartheta$ .  At high frequencies $\left(\lambda\rightarrow0\right)$ ), $\vartheta\,\rightarrow\,\pi/2,$ , and the two cornponent uniform  plane  waves are propagating in directions  nearly parallel to the guide axis $(y)$ .  The wave-guide fields approach some­ thing very  much like a uniform  plane wave  (though  the side-wall boundary conditions prevent it from actually becoming one ; see Eqs. 7 . 1 3 1 ,  7. 133,  7 . 1 34,  and  7 . 1 37  as $\lambda\,\rightarrow\,0\,$ ).  When  the frequency is lowered to $\omega_{m,0}\ \left(\lambda\,=\,\lambda_{m,0}\right),\ \vartheta\,=\,0$ , and the two-component uniform plane waves are propagating directly across the transverse face of the guide, at normal incidence to the side walls.  There is no $\mathcal{Y}$ yariation of the fields $(\uplambda_{g}=\infty$ ) and $\mathrm{II}_{z}\,=\,0$ ; energy simply rattles hack amI forth hct\\'een  the side walls, making no progress dO\m the guide at all. Under this condition, $a\,=\,(m\lambda_{m,0})/2\,=\,m(\lambda/2)$ , so the boundary con­ ditions of Eq. 7. 1 2G demand that $\lambda_{z}$ equal the free-spaee wave length A at this frequeney $\left(\omega_{m,0}\right)$ .  Further lowering of the frequeney ",ill result in the requirement $a<m\uplambda/2$ , or $\uplambda_{z}<\uplambda$ , for which the side walls force n.  compres::;ed waye length condition along z.  We expect, therefore, that the two component plane W:lves \\'ill become nonuniform and will produee attenuation along the guide axis $(y)$ .  This docs in fact oecur.  

Among the $\mathrm{TF}_{m,0}$ \\'[l\'es that we have found ,  it is clear from Eq. 7. 1 38 that, for a gi\'en gu ide dimension $^{\footnote{I n t h i s p a p e r,w e h a v e a p e r,w e h a v e a s s u m e a r e a r i m p i c a t i o n s c e,w e h a v e a s s u m e a r e a r e a r t h e c o m p e r f o r m a n c e.T h e p o r m a n c e u n d e r i m p e r f e c t i o n s a n d w a r e a r e a r e a r e a r m o n s t r a t i c a l w o r k f u r t h e r i m p e r f o r m a n c e.T h e p o r m a n c e u n d e r i m p e r f o r m a n c e c o m p l e t e r m i n T a t i o n s w o r t h e r e a r b i n m p r o b l e t e r m a n d b a c k s c a t t e r l a i n v a l i n t h e r e a r i o m p l e x i s m a n d t h e r e f e r i m p o r m a n c e.T h e p o r m a n c h$ , the $\mathrm{TF}_{1,0}$ $\left(m\right.=1)$ mode has the lowest eutoff frequeney WI .a :  

$$
\omega_{1,0}=\frac{\pi}{a\sqrt{\epsilon\mu}}\qquad\lambda_{1,0}=2a\;\;\;\;\;\;\;\;\;\;\;(b\,<a)
$$  

![](images/3a6963850504bb0d909305593c1913b05e8d2635f8b48f800714f97d1ae87077.jpg)  
Fig. 7.29.  H a ' r<'pl'cspnt:ll ions of $\mathbf{T}\vert\mathrm{:}_{m,0}$ pl'opa).!;al ion in a rectrrngulal' wavc guide. Kote thaI. e:H'h ray in $(a)$ I'('pl'(' ('n l s  hrrIf I h,' fipId  IT<'ngl h of e:wh one in $(b)$ .  

![](images/becce36ecd537497e5da1751a66a300fa8abee59e7e9b441b116644997313fed.jpg)  
F i g .  7.30.  Field lines for $\mathrm{\bfTl}\dot{\mathrm{\bf:}}_{1,0}$ mo,h! in n'dangllhr wave glli,le. $(a)$ Cross section ; $(\flat)$ longitudinal section, along center liIH!; (c) views of top and side phtcs as sccn from inside, showing surfacc-currcnt densities and magnetic ficlds on inncr surfaces.   
Surface-current density  

The fields for the $\mathrm{TE}_{1,0}$ mode undergo only a single half-period varia­ tion acro s the guide from $z=0$ to $z=-a$ .  Some sketches of the field lines from  Eq. 7. 134 for thi  important mode (when $\omega>\omega_{1,0})$ appear in Fig. 7.30.  These field lines arc actually contours to which the instantaneous fields $\pmb{E}$ and $\pmb{U}$ of a single traveling wave are tangent, at some arbitrary moment of time.  The contours are spaced clo ely where the imtantaneous field strength is great.  In Fig. $7.30c$ we have abo shown the wall currents, which clarify the connection between the strong magnetic field at the walls, and the strong electric field (dis­ placement current) along the center regions of the interior.  

It turns out, from an extended analysis of all possible rectangular wave-guide modes which behave exponentially $(e^{\bar{\gamma}_{\mu}})$ along the guide axis $(-y)^{\i}$ that TE solutions exi t with stnl1lling-wavelike field varia­ tions along either or uoth transverse axes ( $\mathbf{\nabla}\cdot\mathbf{\boldsymbol{x}}$ and $z_{.}^{-}$ ) .  These are called $\mathrm{TF}_{m,n}$ modes $(m=0,1,2,\,\cdots;\,n=0,1,2,\,\cdots;$ but not $m\,=\,n\,=0)$ ). This nomenclature for the rectangular guide is based on the convention that the first subscript $(m)$ refers to the number of half-period field variations along a path lJarallel to the u'ide dimension of the cross section, and the second subscript $(n)$ to the number of half-period field varia­ tions nlong a path parallel to the narrow dimension of the cross section. By convention also, the wide dimension is denoted by $a$ , the narrow by $\u_{b}$ (Fig. 7.28b) .  The character of some of these modes, namely, the $\mathrm{TE}_{0,n}$ , is obvious from our solutions here.  Thef'e arc identical in form to the $\mathrm{TF}_{m,0}$ modes, exeept that the "'hole field ::;olution is turned $90^{\circ}$ inside the guide so that the electric field is parallel to t.he l ong dimension (a or z) .  Their cutoff frequencies \\"ill be gi\'en by Eq. 7. 1 : 8 with $_n$ for m and $\upsilon$ for $^{a}$ , but their numerical yalues will be different, e\'en when $n\,=\,m$ ,  because dimension $\upsilon$ is  less  than $^{a}$ .  There arc abo $\mathrm{T}\lambda\ensuremath{\mathrm{I}_{m,n}}$ modes $(m=1,2,\,\cdot\cdot\cdot;n=1,2,\,\cdot\cdot\cdot)$ whidl necessarily h l\'e standing­ \\"a.Yelike fiehl ntriations along both trans\'erse axes.  Among all the TE and T.:'.I solutions, the $T\mathrm{F}_{\bot}(\mathrm{),0}$ has the 100\"C:;t cutoff frequency.  This frequency $\omega_{1,0}$ , gi\'en in Eq. 7. 1 -10, defines, in fad, the 100\'est frequency for which an infinitely long rectang\lla r "'n \'e guide "'il l propagate real po,,'er.  For this reason, the $\mathrm{TI}\dot{\mathrm{:}}_{1,0}$ i:; c t! led the dominant m ode of the w[\\'e guide. [  

It de\'elops that the mode "'ith the next higher cut off frequency is either the $\mathrm{TF}_{0,1}$ or the $\mathrm{{TI}}\mathrm{{:}}_{2,0}$ , depending upon the particula r value of $b/a<1$ .   It is then dear from Eq. 7. 138 that if $b\leq a/2$ , $\omega_{2,0}\leq\,\omega_{0,1}$ and the $\mathrm{{TE}_{2,0}}$ is the mode with the next higher cutoff frequency.  Under these particular  conditions,  in the frequency range $\omega_{1,0}\leq\omega\leq\omega_{2,0}$ $(=2\omega_{1,0})$ only the ${\mathrm{TF}}_{1,0}$ mode can propagate \\"ithout attenuation along the guide axis.  In fact, rectangular mt \'e guides arc normally designed \vith $b\leq a/2$ in order to have this full-octave frequency range for single-mode transmission.  At frequencies above $2\omega_{1,0}$ ,  in a lossless structure, more than one mode may propagate "'ithout attenuation at the same time.  This condition complir'ates considerably the usc of the guide for transmission, and is avoided except in raiher special circum­ stances.  

$\Lambda$ graphical  repre!-!entation  of  the  mul timode  situation described above is shO\m in Fig. 7.3 1 in terms of the yariation of $\beta_{g}$ (or $\alpha_{g}$ ) with frequency W for the  Yarious possible modes.  Analytically,  for the $\mathrm{TE}_{m,0}$ waves, we haye from Eqs. 7. 133, 7. 1 3 1 ,  and 7. 138 (or 7. 13G and 7 . 138),  

$$
\begin{array}{l}{\displaystyle\beta_{g}=\frac{2\pi}{\lambda_{g}}=\frac{2\pi}{\lambda}\,\sqrt{1-\left(\frac{\lambda}{\lambda_{m,0}}\right)^{2}}}\\ {\displaystyle\qquad=\,\sqrt{\epsilon\mu}\,\sqrt{\omega^{2}-\omega_{m,0}^{\ 2}}\qquad\quad\omega\ge\omega_{m,0}}\\ {\displaystyle\alpha_{g}=\sqrt{\epsilon\mu}\,\sqrt{\omega_{m,0}^{\ 2}-\omega^{2}}\qquad\quad\omega\le\omega_{m,0}}\end{array}
$$  

[ Sometimes, the nomenclature of wave-guide modes is chosen to emphasize which field has a longitudinal component rather than which one does not have such a component.  In that case, $\mathrm{TF}_{m,n}$ modes are called $\mathrm{II}_{m,n},$ and $\mathrm{TM}_{m,n}$ modes are called $\mathrm{I}\dot{z}_{m,n}$ .  In rectangular guide, then, the $\boldsymbol{\mathrm{II}}_{1,0}$ mode is dominant.  

![](images/67afdfd325c467c696956be5961ccb980465106ec39f7712ee323dc89d68a7ad.jpg)  
F i g. 7.3 1 .   Attcnu:ttion $(\alpha_{g})$ :tne! phase $(\beta_{g})$ constants vcrsus frcflucncy w for modes in a lossless rcctangular wave gui,Je with narrow dimension not exceeding half the wide one.  Note $\beta_{\xi m,n}<\omega\sqrt{\epsilon\mu}$ and $\alpha_{\ell m,n}<\omega_{m,n}\sqrt{\epsilon\mu}$ .  

These relations contain some adJitionnl interesting information, also discernible in Fig. 7.3 1.  

Above cutoff frequency, the phase velocity along the guide axis is greater than that of light in the medium filling the guide :  

$$
\begin{array}{r}{v_{\mathrm{phase}}\equiv\frac{\omega}{\beta_{g}}=\frac{1}{\sqrt{\epsilon\mu}}\Bigg[\frac{1}{\sqrt{1-(\omega_{m,0}/\omega)^{2}}}\Bigg]}\\ {\mathrm{~\,~\,~\,~\,~\,~\,~\,~\,~\,~\,~\,~\,~\,~\,~\,~}\,>\frac{1}{\sqrt{\epsilon\mu}}\overbrace{\mathrm{~\,~\,~\,~\,~\,~}}^{\mathrm{~\,~~\,~\,~}}\mathrm{~for~}\omega\geq\omega_{m,0}}\end{array}
$$  

The fact that the phase velocity depends upon frequency makes the wave guide a dispcrsivc (though l ossless) transmission system.  Because there is no attenuation under these conditions, hO\\'e\'er, the idea of group velocity has a valid meaning (sec Chapter 5).  For the case at hand,  

$$
r_{\mathrm{{group}}}\equiv\left({\frac{\partial\beta_{g}}{\partial\omega}}\right)^{-1}=\left({\frac{\omega{\sqrt{\epsilon\mu}}}{\sqrt{\overline{{\omega^{2}-\omega_{m,0}}}^{2}}}}\right)^{-1}={\frac{1}{\epsilon\mu}}\left({\frac{1}{v_{\mathrm{{phase}}}}}\right)\ ={\frac{\sin{\vartheta}}{\sqrt{\epsilon\mu}}}
$$  

or  

$$
v_{\mathrm{group}}v_{\mathrm{phase}}\,=\frac{1}{\epsilon\mu}\,=\,v_{\mathrm{light}}{}^{2}
$$  

This is to say, the free-space light \'Clocity $1/\sqrt{\epsilon\mu}$ is the geometric mean between the \Y[\'ve-guide group and phase \'Cl ocities .  Whereas the guide phase velocity always exceeds that of light in the medium filling the guide, the group velocity never docs so.  Indeed the group velocity is just the speed of light in the medium fill ing the guide, pro­ jected al ong the guide axis from the ohlique angle of bounce .  

We have j ust learned that electromagnetic  waves can  be  guided al ong one axis hy con fining them from spread ing in other directions "'iih the aid of entirely opaque  (metal)  walls.  The now relatively common  phenomenon  of  extraordinary  l ight  transmission  through soli<l lutite rods  suggests  that much  Icss  stringent  trans\'erse  con­ straints will rmffice to guide elect romagnetie energy along a single solid. The analysis of some such situations follows.  

# 7.5.2  Nonmetallic Wave Guides \*  

The possibility  of  tota l  reflect ion  arises  at  the interface between difrerent lossless diel ectrics \\·hen incidence occurs on the side with the greater index of refraction.  This suggests that a slab (or perhaps even a roc!) of sueh material \\"ith a high index of refraction may be ahle to confine and guide electromagnetic waves by suecessive internal reflec­ tions at angles $\vartheta_{1}$ beyond the rri tical angle.  The idea is iIIustrated for $\mathfrak{a}$ dielectric slab in Fig. $7.32a$ , to which the nonuniform pl ane-wave pat­ tern of Fig. 7.2G presum ahly applies not only for $z>0$ but also for $z<-a$ (with an appropriate exchange of "left" for "right" ) .  

Analytical determination of t h e  eonditi ons for guidance along the $-y$ direction requires appl ication of houndary cond itions at both $z=0$ and $z=-a$ .  The '1':' I ease (magnetic field paral lel to the houndaries) is t o he t reat ed here, Eqs. 7. 12 1 being t h e  rele\'ant field expressions pertinent to that part of medium 2 in the region $z>0$ .  In the part of med ium 2 occupying $z<-a$ ,  hO\\'ewr, $\pmb{\alpha}_{2}$ must be directed  hft, to make the solution vanish at $z\,=\,-\,\infty,$ .  Othel'\\'iC'e the entire field could hardly be considered "confined" to the slab in the $\pm z.$ -directions.  ?\aturally Snell's law $(\mathbb{E}_{1}.~7.117a)$ applies at both boundaries.  

The equivalent transmission l ine in Fig. $7.27b$ accounts for the $^z$ -axis features of the problem in regard to medium 1 and the boundary condi­ tions at $z\,=\,0$ .  The tangential field continuity conditions at $z=-a$ a re represented i n  the equivalent transm iC'sion line by terminating the line on the left $(z=-a)$ ) in the same impedance as on the right $(z=0)$ ) . This step nppears in Fig. 7.32/J, j ustified by the symmetry of the entire problem about the plane $z\,=\,-\,\textstyle{\frac{1}{2}}a$ .  

According to Eqs. $7.123a$ and 7. 1 2 1, we know the reflection coefficient ${\bar{\Gamma}}_{R^{'}}$ looking to the right at $z=0$ .  The reflection coefficient looking to the right at $z=-a$ is accordingly required by the transmission line for medium 1 to be  

![](images/aba3a1241198c99a4467501fc9526141c6d8f30b5e6d7df08e4ec8dbce33671a.jpg)  
Fig. 7.32.  Dielectric  1ab (mc<lium 1) as a wave !!;uille.  (a) l\1cchanism of  uc­ cessive total internal reflection ; $(b)$ transmission-lille rcprcsclltatioll with respect to $^z$ -axis; 1',:\1 case, II parallel to ooull<laries.  

$$
\bar{\Gamma}^{\prime}(-a)\,=\,\bar{\Gamma}_{R}{'}e^{-j2\beta_{z}a}\,=\,e^{j(\psi^{\prime}-2\beta_{z}a)}
$$  

where we ha\'e written $\beta_{z}\,\equiv\,\beta_{\mathrm{line\,1}}\,=\,\beta_{01}\,\cos\vartheta_{1}$ for convenience.  

On the other hand, looking to the left at $z\,=\,-a$ , we must sec the same load impedance ${\bf Z_{2}}^{\prime}$ us uppears in the ca\c;ulation $7.123a$ for ${\bar{\Gamma}}_{\!{\scriptscriptstyle R}}{'}$ .  

# 380  ELECTROMAGNETIC ENERGY TRANSMISSION AND RADIATION  

Inasmuch as "looking to the right" and "looking to the left" at a. given point on the line merely exchanges the roles of "incident" and "re­ flected"  waves, the corresponding reflection coefficients are simply reciprocals of each other, as pointcd out in Chapter G (Eq. G.15).  The presence of $\mathbf{Z_{2}}^{\prime}$ at $z=-a$ therefore requires  

$$
\bar{\Gamma}^{\prime}(-a)\,=\frac{1}{\bar{\Gamma}_{\!R}^{\phantom{\prime}}{}^{\prime}}
$$  

In view of Eqs. 7.144 and 7. 145 then,  

or  

$$
\begin{array}{l}{{e^{j(\psi^{\prime}-2\beta_{z}a)}=e^{-j\psi^{\prime}}\nonumber}}\\ {{\nonumber}}\\ {{e^{j2(\psi^{\prime}-\beta_{z}a)}=+1}}\end{array}
$$  

It follows that  

$$
\psi^{\prime}-\beta_{z}a\,=\,k\pi\,\qquad\quad k\,=\,0,\,\pm1,\,\pm2,\,\cdots
$$  

which, by Eq. 7.124, becomes  

$$
\frac{n\pi}{2}-\tan^{-1}\left(\frac{{Z_{1}}^{\prime}}{X_{2}}\right)=\frac{\beta_{\it z}a}{2}\ \ \ \ \ \ \ \ n=+1,+2,\cdots
$$  

and  

$$
\frac{p\pi}{2}+\tan^{-1}\left(\frac{Z_{1}{'}}{X_{2}{'}}\right)\,=\,-\,\frac{\beta_{z}a}{2}\qquad\quad p\,=\,0,\,+1,\,+2,\,\cdots_{\perp}
$$  

Use of $\pmb{n}$ and $_{p}$ in Eqs. 7. 147a and 7. 147b is for the purpose of separating explicitly the cases for negative and positive values of $\boldsymbol{k}$ respectively in Eq. 7. 14Gb.  Inasmuch as $\beta_{z}$ must be positive for Eq. 7. 144 to be correct, however, only Eq. 7.147a is appropriate here (bear in mind that $0\le\tan^{-1}\left({Z_{1}}^{\prime}/{X_{2}}^{\prime}\right)\le\pi/2$ according to Eq. 7.124).  Thus con­ sidering separately odd and even values of $\pmb{n}$ in Eq. $\mathbf{7.147}a$ , we find  

$$
\begin{array}{l}{{\displaystyle{\frac{X_{2}}{Z_{1}'}=\,+\tan\frac{\beta_{z}a}{2}}\qquad\quad n\,=\,1,3,5,\,\cdots}}\\ {{\mathrm{}}}\\ {{\displaystyle{\frac{X_{2}}{Z_{1}'}=\,-\cot\frac{\beta_{z}a}{2}}\qquad\quad n\,=\,2,4,\,\cdots\,}}\end{array}
$$  

In the interests of examining the "guide wa.ve length" $\uplambda_{g}(\equiv\uplambda_{y})$ or the guide propagation constant $\beta_{g}(\equiv\beta_{2}\equiv2\pi/\lambda_{g})$ as functions of fre­ quency $\omega$ , we shall write the function $X_{2}^{\prime}/Z_{1}^{\prime}$ as follows from Eqs.  

$7.109a$ , 7.122, $7.121a$ , and the definition $\beta_{z}\,=\,\beta_{01}\cos\vartheta_{1}$  

$$
\frac{{X_{2}}^{\prime}}{Z_{1}{'}}=\frac{\alpha_{2}}{\omega\epsilon_{2}\eta_{1}\left(\frac{\beta_{z}}{\beta_{01}}\right)}=\frac{\sqrt{\beta_{g}{'}^{2}-\beta_{02}{}^{2}}}{\beta_{z}}\left(\frac{\epsilon_{1}}{\epsilon_{2}}\right)
$$  

But in medium 1  

$$
\beta_{g}{}^{2}+\beta_{z}{}^{2}=\beta_{01}{}^{2}=\omega^{2}\epsilon_{1}\mu_{1}
$$  

so Eq. 7. 149 becomes, upon eliminating $\beta_{g}{^2}$ ,  

$$
\frac{X_{2}{}^{\prime}}{Z_{1}{}^{\prime}}=\frac{\epsilon_{1}}{\epsilon_{2}}\,\sqrt{\left(\frac{\beta_{01}{}^{2}-\beta_{02}{}^{2}}{\beta_{z}{}^{2}}\right)-1}
$$  

Equation 7 . 15 1  expreSiies $X_{2}^{\prime}/{Z_{1}}^{\prime}$ as :1 function of $\beta_{z}$ [or $(\beta_{z}a)/2]$ for any gi\"Cn frequen cy $\omega$ (,,·hich fixes $\beta_{01}\,=\,\omega\sqrt{\epsilon_{1}\mu_{1}}$ and $\beta_{02}\,=\,\omega\sqrt{\epsilon_{2}\mu_{2}})$ . This allo,,·s :1 graphiC'al solution of Eqs. $7.1\!\cdot\!18a$ or $7.148b$ for the quantity $(\beta_{z}a)/2$ at the frequency $\omega$ .  The gra phical solution entails plotting both sides of Eqs. $7.1\48a$ amI 7. 1-i8b against $(\beta_{z}a)/2$ on the same abscissa to determine intersection points.  Figures $7.33a$ and $7.33c$ rcspectively present these solutions $(\bigcirc)$ for three different fre(lUencies $\omega_{\angle1}<\omega_{B}<$ $\omega_{C.}$ , pertaining to the cun'es marked $\mathit{{A}}\mathrm{,}\;\mathit{{B}}_{\mathit{{z}}}$ and $C$ respectively.  Figure $7.33\time10$ shows the calculation of $\beta_{g}$ from Eq. 7 . 1 50.  This equation plots as a circle , rel:J.ting $\beta_{g}$ t o $\beta_{z}$ , having a radius directly proportional to $\omega$ . The important restriction from Eq. 7 . 1 5 1  that  

$$
0\,\leq\beta_{z}\,\leq\sqrt{{\beta_{01}}^{2}-{\beta_{02}}^{2}}\,=\,\omega\sqrt{\,\epsilon_{1}\mu_{1}\,-\,\epsilon_{2}\mu_{2}\,}
$$  

should not be overlooked.  It defines the points at ,yhich curves $A,B_{z}$ , and $c$ strike the a.bsciss a.in Figs. 7.33a and 7.33c.  Nor should its con quences from Eq. 7.150 be neglected:  

$$
\beta_{02}<\beta_{\ell}<\beta_{01}
$$  

The guide waye length akays mllst lie bc{tcccn that of free-space uni­ form plane wans (or light) in medium 1 and in medium 2.  Similarly, the g\lide phase YeloC'ity exceeds that of light in medium 1 (with the higher refra ctive index) , Lut is less than the (greater) light velocity in medi\lm 2.  

Although no generally valid  analytical relation for $\beta_{g}(\omega)$ m ay be written in the present circumstances, a  study of Eqs. 7 . 1 5 1 ,  7. 148, 7. 150, and Fig. 7 .33 provides satisfying insight into the effect of fre­ quency variation when the dimension $^{\footnote{I n t h i s p a p e r,w e h a v e a s s u m e a s s i n g a u t h o r.T e l:~+86-1088236095095.E-m a i l a d d r e s s:t a n g q u a n c e286256b y a n s c e.T e l r a n s a n a n d d e a n a r e s s u m p e r f o r m a n c e c o n a n d d e a n d b y t r a n s i t t h e c a l w o r k~.}$ is fixed .  At a high fre<1uency $\omega_{C}$ , the CUlTe (Eq. 7. 151) extends over a large range of $\beta_{z}$ , because the upper bound  (Eq. 7. 132) incre[lC:cs d i rcctly with $\omega$ .  There arc then many int er!:'ect ions $\mathrm{[^{\prime\prime}}$ through $\overline{{{\u}}}^{\prime\prime}$ )  of t he  C 1 I I"\"(':';  in  Figs. $7.33a$ and $7.33c$ , \"hich repre>'ent f'ol u t i ons to  Eq". 7. 1 I S .   E\'idently many of the"e T:\ I waves can prop:lg:t1 e  toget her along the "lab at high fre­ quencies.  

![](images/f683b7d51ddb376f368e88588e80e666090948d652067d6687a0abd951a7f4e2.jpg)  
Fig. 7.33.  Solution for T:\I-wltvc PJ"op:tglttion constltnts for Fig. 7.32.  (a) , (b) , and (e) represent Eqs. 7. 1·!8a :we! 7. 1 5 1 ,  Eq. 7 . 1 50, Itn[1 Eqs. 7. 1 4 8b ant! 7. 1 5 1  respec­ tively.  Points market! (0) are solut ions for $\beta_{z}$ .  Parts $(a)$ Itnt! $(b)$ :dso apply to T:\[ waves, ane! (e) ane! $(b)$ t o TE waves, for Fig. 7.35.  

J\s frequcncy is l m\"('rpd ('on t ill\l()U. ly, 1 1lP \'[l l'iou>' i n t er:-:ect ion points in Figs. $7.5_{\cdot}^{\cdot}\cdot\mathrm{3}a$ and I.:::lc :"lide dOl\'l1\\';II'(!  (:-:('c  points $1^{\prime\prime},\,1^{\prime}$ ,  and  I ,  or $\pmb{2^{\prime\prime}}$ and $2^{\prime}$ ) , each on i t s  O\\'Jl (po:-:i t in') hranch of t he tan or - eot func­ tion.  Ac'('ordingly \\'C  ca n i( kn t i fy c;[('h :-:uch (po:-:i t i\'( ) braneh "'itlt a field solution  or "mode" who:-:c propprt ies (·hangc conti nuously with frequency.  A t  lca"t this appears to he the case for any such branc'lt until a frequency is reac·hed for \"hidl the int er:-:cc:tion arri\'es at the abscis:oa.  (Hefer to points $2^{\prime\prime}$ am! ${\mathcal{Z}}^{\prime}$ on curves $\boldsymbol{C}$ am! $B$ in Fig. $7.33c$ , and then especially to cur\'e $\angle1$ there.)  Any addit ional lowering of the fre­ queney suddenly lc:l\'es us \"ith no solution corresponding to this mode! The u'QL'e 7mdcr consideration sim ply ceases to exist.  

In surpri::;ing contrast  with  our  metal  \\'a\'e-guide  solutions,  the present ones do not go into an a t t enua ting condition below cutoff, but rather reach a cuto('[ (or critical) condition and vanish forthwith from t he sccne.  

Tlw expla nation for t his Iwha\'ior is found hy computing the angle $\vartheta_{1}$ i n  Fig.  7.32 at the critical frequen('y $\omega_{\mathrm{crit}}$ of a ny mode.  At such frcquC'I1(,Y, the end point of validity of 1-:q. 1. 1;') 1  fal l s  at the base of $\mathfrak{a}$ posi t i \'l  hr:lJlch of the tan or - ('ot fUllC'tion, as \\'(llIld occur for example a t  a frequen('y bet,,-ecn $\omega_{\bullet}\mathbf{1}$ amI $\omega_{\beta}$ on hranc·h $2^{\prime\prime}{-}2^{\prime}$ in Fig;. $7.33c$ .  Then from Eq. 7. 1;') 1  

$$
\beta_{z_{\mathrm{crit}}}^{2}=\beta_{01_{\mathrm{crit}}}^{2}-\beta_{02_{\mathrm{crit}}}^{2}
$$  

and from Eq. 7.150  

$$
\beta_{\mathrm{gcrit}}^{2}\,=\,\beta_{\mathrm{01crit}}^{2}\,-\,\beta_{z\mathrm{crit}}^{2}\,=\,\beta_{\mathrm{02crit}}^{2}
$$  

But in general  

$$
\beta_{g}\,=\,\beta_{01}\,\sin\vartheta_{1}
$$  

so  

$$
\sin\left(\vartheta_{\mathrm{1crit}}\right)=\frac{\beta_{\mathrm{{gerit}}}}{\beta_{01\,\mathrm{{crit}}}}=\frac{\beta_{\mathrm{02crit}}}{\beta_{\mathrm{01crit}}}=\frac{v_{1}}{v_{2}}
$$  

This result sho\\':; that at the critieal frequency, the internal reflections have j ust re;tche(l the cri t ical angle.  Any lower frequency will bring the inc ident angle helO\\' critical, and there will be no basis for confining the \\'a\'CS to the slab.  

$\therefore$ calculat ion of t he  cTit ical frequen(,ies in terms of the geometry t erns from recogn izing th lt the in terscdion poi nts on Fig,;. $7.33a$ and $7.33c$ fal l :I t zeros of the ta n  or  - ('ot fllnetions, in  add ition to being  

# 384  ELECTROMAGNETIC ENERGY TRANSMISSION AND RADIATION  

end points of curves like $A,\,B_{\mathrm{i}}$ , or $\boldsymbol{C}$ .  These zeros, in both figures, can be summarized by the statement  

or  

$$
\begin{array}{l}{{\beta m_{\mathrm{{erit}}}=\displaystyle\frac{m\pi}{a}\qquad\quad m=0,1,2,\,\cdots}}\\ {{\qquad}}\\ {{\qquad\lambda m_{\mathrm{{erit}}}=\displaystyle\frac{2a}{m}\qquad\quad m=0,1,2,\,\cdots}}\end{array}
$$  

even values of $\mathbf{\nabla}m$ arising from Fig. $7.33a$ and odd values of $^{m}$ from Fig. $7.33c.$ .  With Eq. 7. 154, Eq. 7. 157 becomes  

$$
\omega_{m_{\mathrm{erit}}}=\frac{m\pi}{a\sqrt{\epsilon_{1}\mu_{1}\,-\,\epsilon_{2}\mu_{2}}}\,\qquad m\,=\,0,\,1,\,2,\,\cdots
$$  

The existence of one  T::\I solution which persist down to zero fre­ quency is a remarkable feature of these results.  It occurs in the case $m\,=\,0$ in Eq. 7. 158, leading to $\omega_{\mathrm{0_{crit}}}=0$ .  This solution corresponds to branch $1^{\prime\prime},\,1^{\prime},\,1$ , in Fig. $7.33a$ .  Thus very low frequency waves may, in principle, be guided by a dielectric sheet.  

Defore extrapolating this conclusion any further, however, attention is directed to the fact that for any l\\I mode at high frequencies  

$$
\beta_{g m}\,\underset{\omega\to\infty}{\longrightarrow}\,\beta_{01}\,=\,\omega\sqrt{\epsilon_{1}\mu_{1}}
$$  

This follows from the feature of Figs. $7.33a$ and $7.33c$ that  

$$
\begin{array}{c c}{{\beta_{z m}\displaystyle\sum_{\omega\to\infty}\frac{(m+1)\pi}{a}~~~}}&{{~~~m=0,1,2,\cdots}}\end{array}
$$  

which remains finite, while in Eq. $7.150\,\beta_{01}$ (and hence $\beta_{g.}$ ) approaches infinity with $\omega$ .  At high frequencies, then, one expects most of the real longitudinal power flow to occur within the slab (medium 1), inasmuch as its phase velocity dominates the longitudinal propagation.  A check upon this conclusion is supplied by the relation  

$$
\alpha_{2}=\sqrt{{\beta_{g}}^{2}-{\beta_{02}}^{2}}\underset{\omega\to\infty}{\longrightarrow}\omega\sqrt{\epsilon_{1}\mu_{1}-\epsilon_{2}\mu_{2}}\underset{\omega\to\infty}{\longrightarrow}\infty
$$  

The penetration of the field into medium 2, outside the slab, becomes arbitrarily small at high frccluencies as the transverse attenuation be­ comes indefinitely large.  

On the other hand, Eqs. 7.161 and 7.155 show that  

$$
\begin{array}{r l}{\beta_{g}=\beta_{02}\Big\}&{{}\quad\mathrm{at}\;\omega\,=\,\omega_{\mathrm{crit}}}\end{array}
$$  

The field extends uniformly to infinity outside t h e  sbb, in medium 2, at the critical frequency.  An infinite amount of rcal l ongitudinal powcr is carried outside medium I !   :\ 1edium 2 dominates thc l ongitudinal propagation constant [Eq. 7 . W2aJ .  The  pread of the field outmtnl from the slab increases as frequcncy drops tU\\'ard the critical one, even if the critical frequency is zcro.  \\,hile the I U\\'est '1':\1 mode can there­ fore in principle be exeitcd at vcry low frequcncies, the extension of the field far beyond the slab requ ircs that any source supply large amounts of total power to do so.  .Just as is the ca "e in any critical rcflection $(a t$ the critical angle) , the field in medium 2 at frequcncy $\omega_{\mathrm{crit}}$ becomes a uniform plane wave tnn'eling along $-y$ .  "'hen $\omega_{\mathrm{crit}}=0_{\mathrm{.}}$ , this bchavior is approached ,  but never actually rcached, as $\omega\,\longrightarrow\,\omega_{\mathrm{crit}}=0$ .  

An examination of Fig. $7.32\time10$ ::-ho\\'i:i the ::;tanding-mt ve character of the field distribution acro::;s the $\textit{\textbf{z}}$ dimension of the slab (in medium 1 ) . The impedance $\mathbf{Z_{2}}^{\prime}$ i s  a function o f  frequency (::;ee Eqs. 7. W 1  and 7 . 1G2) :  

$$
\mathrm{Z}_{2}^{\prime}\underset{\omega\rightarrow\infty}{\rightarrow}-j\eta_{2}\;\sqrt{\left(\frac{v_{2}}{v_{1}}\right)^{2}-1}
$$  

$$
\mathrm{Z}_{2}^{\prime}\xrightarrow[\omega\rightarrow\omega_{\mathrm{crit}\neq0}]{}0
$$  

Equation 7. 1G3b makcs clear thc reason for the "half-\\'ave" cond it ions (Eq. 7. 157) at the  critical frequency.  It abo clarifies the fact that $\mathrm{E}_{y2}=0$ ,  which supports  the previous contention  that the field  in medium 2 is a uniform plane wave tnLYeling al ong $-y$ at this frequency. Characteristically different from the modes in a  mctal \\'aYe guide, these modes do change thcir ficld distrilmtions ovcr the guide cross sec­ tion as frequency is alterell.  Conccntratcd strongly within the slab at high frequencies, the field cnergy of a given mode spreads laterally into the surrounding space as the frequency is lowered until, finally, at the critical frequency, it has spread to infinity and no further guided wave of that mode can be supported at reduced frequencies.  

Sketches of $\beta_{g}(\omega)$ for the various '1'::'1 1 modes discussed can be made essentially by visualizing carefully  Fig. 7.33 and n oting E<lS. 7 . 1 53, 7 . 1 59,  7 . 1 GO,  and $7.162a$ .  In this connection it helps,  however,  to consider analytically the slope $(d\beta_{g}/d\omega)\,={v_{\mathrm{group}}}^{-1}$ ,  implicitly defined by Eqs. 7. 148, 7 . 1 5 1 ,  and 7. 150.  From the derivative with respect to $\omega$ of Eq. 7 . 1 50, we have  

$$
\frac{\pm\beta_{g}}{d\omega}=\left(\frac{\beta_{01}}{\beta_{g}}\right)\left(\frac{d\beta_{01}}{d\omega}\right)-\left(\frac{\beta_{z}}{3_{g}}\right)\left(\frac{d\beta_{z}}{d\omega}\right)=\frac{\beta_{01}{}^{2}}{\omega\beta_{g}}-\frac{\beta_{z}}{\beta_{g}}\left(\frac{d\beta_{z}}{d\omega}\right)
$$  

# 386  ElECTROMAGNETIC ENERGY TRANSMISSION AND RADIATION  

Because Fig. 7.33 or Eq. 7. 100 shows that $(d\beta_{z}/d\omega)\begin{array}{c}{{\longrightarrow}}\\ {{\omega\to\infty}}\end{array}0$ for any given mode, and in view of Eqs. 7. 150 and 7.lGO, Eq. 7. 104 tells us that  

$$
\left(\frac{d\beta_{g}}{d\omega}\right)_{\omega\to\omega}\to\frac{\beta_{01}}{\omega}=\sqrt{\epsilon_{1}\mu_{1}}=\frac{1}{v_{1}}
$$  

The group velocity at high frequencies is dominated by the medium (medium 1) in which most of the energy is concentrated at these fre­ quencies.  

At the critical frequency, however, Eqs. 7.lG2 and 7.1S4 convert Eq. 7.104 to read  

$$
\begin{array}{r l}&{\left(\frac{d\beta_{g}}{d\omega}\right)_{\omega_{\mathrm{crit}}}=\frac{\beta_{01}}{\beta_{02}}\left(\frac{d\beta_{01}}{d\omega}\right)_{\omega_{\mathrm{crit}}}\!\!\!-\left(\frac{\sqrt{\beta_{01}}^{2}-\,\beta_{02}^{2}}{\beta_{02}}\right)_{\omega_{\mathrm{crit}}}\!\!\!\left(\frac{d\beta_{z}}{d\omega}\right)_{\omega_{\mathrm{crit}}}}\\ &{\left(\frac{d\beta_{g}}{d\omega}\right)_{\omega_{\mathrm{crit}}}\!\!\!=\frac{\nu_{2}}{v_{1}}\left[\frac{1}{v_{1}}-\,\sqrt{1-\left(\frac{v_{1}}{v_{2}}\right)^{2}}\left(\frac{d\beta_{z}}{d\omega}\right)_{\omega_{\mathrm{crit}}}\right]\,}\end{array}
$$  

or  

where it is undcrstood that the derivatives are taken as limits for $\omega\longrightarrow\omega_{\mathrm{crit}}$ only.  

To compute $d\beta_{z}/d\omega$ , note that from the right side of Eq. $7.148a$ we have on one hand  

$$
\frac{d}{d\omega}\left(\tan\frac{\beta_{z}a}{2}\right)=\frac{1}{\cos^{2}\left[(\beta_{z}a)/2\right]}\frac{a}{2}\frac{d\beta_{z}}{d\omega}
$$  

with a I:'imila r rcsult for Eq. 7.1 18u :  

$$
\frac{d}{d\omega}\bigg(-\cot\frac{\beta_{z}a}{2}\bigg)=\frac{1}{\sin^{2}\big[\big(\beta_{z}a\big)/2\big]}\frac{a}{2}\frac{d\beta_{z}}{d\omega}
$$  

On the other hand, frum the left Sillc of E(Pi. 7.US, making use of Eq. 7. 151, we find  

$$
\frac{d({X_{2}}^{\prime}/Z_{1}^{\prime})}{d\omega}=\frac{\epsilon_{1}({\beta_{01}}^{2}-{\beta_{02}}^{2})}{\epsilon_{2}r{\beta_{z}}^{3}}\left(\frac{\beta_{z}}{\omega}-\frac{d\beta_{z}}{d\omega}\right)
$$  

\"ith  

$$
r\equiv\sqrt{\left(\frac{\beta_{01}{}^{2}-\beta_{02}{}^{2}}{\beta_{z}{}^{2}}\right)-1}
$$  

That iI:', the yalne of $d\beta_{z}/d\omega$ is computed by equating E<}s. 7. 107 and $7.168a$ , ,,'hich yields  

$$
\frac{d\beta_{z}}{d\omega}=\frac{\beta_{z}}{\omega}\Bigg(\frac{1}{1+\{(a\epsilon_{2}\beta_{z}^{~3})/[2\nu^{2}\epsilon_{1}({\beta_{01}}^{2}-{\beta_{02}}^{2})]\}}\Bigg)\;\leq\frac{\beta_{z}}{\omega}
$$  

where  

$$
\nu\,=\,\cos\,\left(\beta_{z}a/2\right)\,\mathrm{or}\,\sin\,\left(\beta_{z}a/2\right)
$$  

according to whether we are dealing with Err. $7.148a$ or 7.14Sb respcc­ tively.  

In  the  particular  case $\omega\rightarrow\omega_{\mathrm{crit}},$ ,  we  o1>:;c1'\'e  that $\nu^{2}\to1$ and $\beta_{z e r i z}$ is givcn by Errs. 7.154 and 7. 157.  So Eq. $7.169a$ becomes  

$$
\left(\frac{d\beta_{z}}{d\omega}\right)_{\omega\to\omega_{\mathrm{rit}}}\!\!\!=\sqrt{\epsilon_{1}\mu_{1}\,-\,\epsilon_{2}\mu_{2}}\,=\frac{1}{v_{1}}\,\sqrt{1\,-\left(\frac{v_{1}}{v_{2}}\right)^{2}}
$$  

\\·hich giws I 1 S  in Eq. 7. 1(iG  

$$
\left(\frac{\d\mathcal{l}\beta_{s}}{\d\mathcal{l}\omega}\right)_{\omega_{\mathrm{crit}}}=\frac{1}{\d\tau_{2}}
$$  

Again, the grol1p wlo('ity i s  domi natcd b y  the mcdium in \yhich most of the field encrgy is conccntrated .  

![](images/bdb0b3c593f1c725afb794be323bd83cc3824334ee2a3a273427ed40735be13c.jpg)  
F i g .  7.34.  l'J .as(' ronst anh $\beta_{{y m}}$ \"('rsu  frrclupnry w for T:'I[ Illodf's for Figs. 7.32 and 7.a:l.  S:lIlU' g(,'H'r:d  form,  \I·i t  J. S:l!lln  ni t i l"d  fn'qu(,'H'i('s $\omega_{m}$ . applies lo TE wav('s.  lI','('/I-0/"f1t.,. mod,·s also apply to '1' :'I [  waves for Fig. 7.3ii.  Odd-order moues abo a pply to '1'1-: 11-:1'';('S fur Fig. 7.3ii,  

# 3 8 8   ELECTROMAGNETIC ENERGY TRANSMISSION AND RADIATION  

At intermediate frequencies $\omega_{\mathrm{crit}}<\omega<\infty$ , Eqs. 7. 1G4, $7.109a$ , and 7. 150 show that  

$$
\frac{d\beta_{g}}{d\omega}\ge\frac{\beta_{01}^{~2}}{\omega\beta_{g}}-\frac{\beta_{z}}{\beta_{g}}\bigg(\frac{\beta_{z}}{\omega}\bigg)=\frac{\beta_{g}}{\omega}
$$  

which means that the group velocity cannot exceed the phase velocity in these modes.  

Figure $7.34$ shows the general form of $\beta_{g m}(\omega)$ based upon all the preceding considerations.  It should be compared with Fig. 7.3 1 for the rectangular metal wave guide.  An analysis for TE modes (electric field parallel to the boundaries) yields similar results, with the same set of critical frequencies.  This ease is taken up in the Problems.  

# 7.5.3  Combination Meta l and Dielectric Wave Guid e \*  

As our final example, ,,"e ask whether a perfectly conducting metal surface, upon which is coated a layer of losslcss dielectric, may serve to guide electromagnetic waves.  The configuration is shown in Fig. $7.35a$ .  

The T I case is most interesting, amI we start again with the idea of successi" e  t otal intcrnal  rcflcction  from the boundary  at $\boldsymbol{z}=0$ . In this case, ho,,"c" cr, we shall have metallic reflection at $z\,=\,-a/2,$ , and the equi" alcnt  transmission-line  picture  relevant  to the $\geqslant$ -axis dircctions is shown in Fig. $7.35b$ .  Compare Figs. 7.35 and 7.32.  

Equation 7 . 1H with $a/2$ in place of $^{\footnote{I n t h i s p a p e r,w e h a v e a s s u m e a s s i n g a u t i o n s i t i c a t i o n s e r e l a t i o n s a r e h e p e r f o r m a n c e.T h e p o r m a n c e u n d e r i m p e r f e c t C S I i s w o r t h f u r t h e r i n k e r a n d d e r i v e s a r e c h a n n e r g y t h e r i c r i c a t i o n.I n t h i s w o r k,w e a c t i v e l y i n t r o a s e r e a r e d i r e c e i v e r a n d t h e r e a l w a n i n g,w e a c t i v e l y i n t r o a s w i t h m o d e r i v e c e i v e s a r e c h a n n e r g y e r f o r m a n c e c o m p a r t i o n.}$ expresses line conditions at $z\,=\,-a/2,$ , looking to the right.  This time, though, we wish $\mathbb{E}_{y1}=0$ at $z\,=\,-a/2$ on account of the metal surface.  Looking to the left there­ fore, the metal rcquircs $\bar{\Gamma}_{\mathrm{{left}}}^{\prime}(-a/2)\,=\,-\,1$ , or looking to the right the metal demands the reciprocal $\bar{\Gamma}_{\mathrm{right}}^{\prime}(-a/2)\,=\,(1/{-1})\,=\,-\,1$ .  Using Eq. 7. 144 ,,-ith this condition, and $a/2$ for $^{a}$ yields  

$$
\bar{\Gamma}^{\prime}\left(-\,\frac{a}{2}\right)\,=\,e^{j(\psi^{\prime}-\beta_{z}a)}\,=\,-1
$$  

which says simply that the metal surface must faJI at a node of $\mathbf{\deltaE_{w1\cdot}}$ Therefore  

$\psi-\beta_{s}a=\pm(2n+1)\pi\qquad n=0,1,2,\,\cdots$ (7.174)  

or in view of Eq. 7.124  

$$
\frac{X_{2}^{~}}{Z_{1}^{~\prime}}=\tan\left(\frac{\beta_{z}a}{2}\right)
$$  

\yhere only positi" e valucs of $\beta_{z}$ arc of intercst.  The rcsult (Eq. 7. 175) is iclentical with Eq. 7. USa.  All other considerations pcrtinent to the details of solution, excluding Eq. 7. l-1Sb and Fig. $7.33c$ , but including Figs. $7.33a$ and 7 .33b, apply to this case.  

![](images/a4438ced892b9fe00a2b59bc89224a8a19cb0dd1c94f034f8eeb83e47f0d1070.jpg)  
Fig. 7.35.  :\1etal  ul'face with dielectric coatin),( (m( diulll 1) as a wave ),(uicle.  (a) :\[echani"lll of  ucces ive refkctiolls, alt('r­ nately  total  intcl'Ilal $\left(z\right)=0^{\prime}$ ) and metallic $(z\,=\,-a/2)$ ) ; $(b)$ transmission-line  r('presenta­ tion with respcct to $z_{\mathrm{:}}$ -axis (1':\1 case, II parallel to boundaries) .  

In the present problem, then, there are only half as m any T:\1 solu­ tions as we had for the dielectric slab alone.  In particular, only the cases of m even in Eq. 7 . 157 apply here.  This is reasonable because, if we consider the solutions to the dielectric slab problem, symmetry re­ quires that half of them \yill have nodes of $\mathrm{E}_{y1}$ at the middle of the slab and the rest will have maximum values of $\mathrm{I}\dot{\boldsymbol{\Sigma}}_{y1}$ at the middle.  The clearest  picture  of  this  i"itlla( ion  O('C \ l l'S  at  the  critical  frequencies (E<1. 7.157) \\"11('re t he slab \rid t h $\boldsymbol{a}$ is SP('Jl to he an am multiple of $(\uplambda_{z}/2)$ for ?It eH'n, but an orlrl lllul( iple of $(\uplambda_{z}/2)$ [or $m$ odd.  With the comments following Eq. 7. W31), i t  i" ('lear that only tho;.:e ;':(Jl ut ions "'ith ?It eyen d o  in faet h:l\'e $\mathrm{I};{}_{\!\prime\!/1}\,=\,0$ on i1w pla ne $z\,=\,-\,a/2,$ , and for the;.:e cases we could slip in an illfillit cl y  t hin cOllduc t i ll f!:  shed on t h i:; plane to aehie\'e a .  solution to our present p rohlem,  The ('I'('n-order CLllTCS of Fig. 7.:n (ckriH'd from Fif!:, 7,:;:;il) :l pply to these 'L\I \\'a\'cs.  It is interc:;ting that onc of t hc solut ions p }'( seIT('d i,-; t hat \\'itll $\omega_{\mathrm{crit}}=0$ ; thus, mbj ect to the genera l power l i m i ta t ion" d is('usscd prc\'iously, the dielectric-coatcll metal shcet can support lo\\'-fre<jucncy gu idcd wavcs of the T I type.  

Since only Fif!:s. $7.33a$ amI 7.3:3h apply to the metal-and-diclectric­ guide  prohlem, there are evid ently  f!:ap:; in  the valucs of $(\beta_{z}a)/2$ covercd  hy these T [  solut ions.  For example $\pi/2<\beta_{z}a/2<\pi$ is not po:;sible.  Thc!'e ga ps " ere " f i l led in" by Fig. $7.33c$ for the d icl ectri c­ sheet elti"e.  In the prci"cnt ('on fig\l l'a t ion, hO\\'e\'cr, a. study of the TE waves (in the Problems) i"ho\\':, that t hey j ust fill in the gaps by kading to Fig. $7.33c$ .  They lead eOlTc;.:pondingly t o  the odd-order CurH'S of Fig. 7.3-1.  This mean;.:, of eOlm.:e,  that the TE ancl T I \\'aH':'; do not have thc  ame el'itical fl'equelwic,; in t hi,; ea e, and that fliNC is no TD ?/lode lchich propagates at very low fr('quencies (i.c., jor u'hich $\omega_{\mathrm{crit}}=0$ ).  

An interesting applicat ion of the 100\'e:-:t T I  mode for "one-\\'ire transmi:-:sion" \\'as fir t made by G oubau L  (Fig. $7.36a)$ .  lIe actually uses the similar solution \\'hi<:ll appl ies t o  a.  round metal \"ire coated with a. dielectric bye I'  (j ust rust or  eorl'osion \"ill sufTi('e, though it is not the most efficient arrangcment) .  The nature of thc field is quite like that of Fig. $7.35a$ if we visualize thc metal and dielectric sheet bcnt around so that thc $x$ -axis becomes the pcrimeter of a eir<:le $\scriptstyle\varphi-$ coordinate) , thc $z_{\mathrm{:}}$ -axis bceomes the radial coord ina t c $\left(\rho\right)$ , and $y$ becomes the longitudinal direction (z) .  The eoat ing is thin, and the field tl ually spreads outward transversely by many wire diameters.   Iost of the powcr is carried outside the wire and coating.  The "la unching" a r­ rangement (Fig. 7.3GiJ) takes t his spreading into account by employing a  coaxial-line feed \\'ith the outl'r  conductor  flared  into a  horn. $\Lambda$ :oimilar "I'eeci\'ing" horn collects tlw pO\\'er  at  the other eIl!l.  The arrangement is cspecially good for  t raig;ht unimpedccl runs, as sug;­ gestell by Fig. $7.3(\mathrm{j}),$ , hut it may hc used uncleI' other eircumstances where  sharp bcnd,.,  or ;.:crious  di;':('ontinuities  do not  occur  too frcqllcnily.  A t   th(';;(\  thc  cri t ic:t1-re fled ion  p;uidancc  featurc  of  the f'yst clll \\"mlld f:l i l ,  alld  ()me l o, s by rad i a t i on \\"cHIld rC 1lI t..  

![](images/541b6ee1612d677cf65ffdd34fa28f1855a19c53f727236efd81b056a5411dd5.jpg)  
F i g .  7.36.  ,\pplirat inn o f  Im\"p t T'\f mod"  nil d i ,'I,,('( ri c-('oat (',\ llwtn\ snrfacc to "olle-wire" I r:lIl'mi" ,inll.  (0 )  Ci rcllI:l r  f01'1ll of $\smash{\Gamma^{\prime}\}_{\ensuremath{\mathbf{n}}^{\prime}}$ , $7.35\times$ ;  (II) Il"   of sill lt  wire, showill  fhred eoa"i:J i horns 10 l:l I l 1] ('h :tlld f'('('!'i n' T'\f mode,  

'Ye ha\"(' ('ollsidcr<,d some of the simplest, examples of \\':lW'S p;1lided by  losskss  Ilwd ia,  In  more  ('ompl ical < d  problems,  the coordinate f'yst cllls may hC('OIll e  m orc ela borate, and mixt ures of T E  and T:\[ \nn'cs top;d hcr may I ll' requ i r<·d to nwcl Ow l Joundary cond i t i ons.  ,rc ha\'c att empt ed t o  f!;O on ly  fa r ('nou h  \\' i t h  f!;uided-\\';L\'C COlH'ept s  to int rod1lcc t hc  m:lj Ol'  poi n t s  of physi (,:t1 sip;ni fie:lllcc, and t o  pla('c on fi rm  ground  our  undcr"t :lIldinf!;  of  uniform  and  nonuniform  plane waves.  Some further elaboration of guided waves is taken up in the Problems.  To treat additional details here would quickly carry us into the realm of specialized methods and studies.  

# P ROBLEMS  

Probl em 7.1 .  (a) Write a complete set of :-Iaxwell's equations for a source-free region with constant parametcrs $\epsilon,~\mu,~\sigma$ (J",  Specialize the equations to the case in which the electromagnetic fichls arc independent of $_x$ and $y$ .  (b) Find the most general solutions to theoe equations for thc z components of the fields and for the charge density,  Undcr what conditions would $\rho\,=\,\rho_{0}$ , a constant,  be a suitable solution?  (c) Find all the degenerate solutions for $\scriptstyle{E_{z}}$ and $\boldsymbol{I}\boldsymbol{I}_{y}$ which have the special forms: (i) $E_{x}=E_{x}(z)$ ; (ii) $E_{x}=E_{x}(t)$ ;  (iii) $I I_{y}=I I_{y}(z)$ ;  (iv) $I I_{y}=I I_{y}(t)$ ,  Hepcat also for $_x$ and $y$ interchanged in (i)-(iv)  above.  (d) Define the necessary and sufficient conditions to be placed upon :\faxwell's equations so that only uniform plane waves will be solutions.  (e) It has been suggested that because of the possi­ bility of solutions (b) ami (c), " light" is not necessarily a t l'llllSVerSe wave phenom­ enon.  Do you agree?  Support your position with examples.  

Problem 7,2.  l\Iake perspective sketches, corresponding to those of Figs. $_{7.1a}$ and $\mathbf{7.1}c,$ showing the orientations o f  t h e  field vectors o f  two orthogonal plane waves traveling in the $-z$ direction.  

Problem 7.3.  ,nth reference to Sec. 7.1 of the text, consider in the time domain the  pair  of  plane  waves, $E_{T A}{}^{+}\,=\,a E_{1}{}^{+}\,+\,b E_{2}{}^{+}$ , $I I_{T A}{^+}={\frac{1}{\eta}}\,_{a_{z}}\times\,E_{T A}{^+}$ and ${E_{T B}}^{+}=c{E_{1}}^{+}+d{E_{2}}^{+},$ , $I I_{T B}+\ =\frac{1}{\eta}\:_{a_{z}}\times\:E_{T B}+$ ,  in  which $a,\ b,\ c,$ and $^d$ are  real constants and ${E_{1}}^{+}$ and ${E_{2}}^{+}$ are oriented respectively in thc $\pmb{\alpha_{x}}$ and ${\pmb{\alpha}}_{y}$ directions. (a) ${E_{1}}^{+}$ and $E_{2}{}^{+}$ are linearly illllependpnt vectors because they lie in difTerent (in fact, perpendicular) directions.  Are $|l_{1}^{\cdot}+|$ and $|\dot{I}\dot{z}_{2}^{+}|$ ahmys linearly indcJlendent't Give examples.  (b) Determine nccessary and sufIieient conditions for ${\bar{E_{T A}}}^{+}$ and ${\vec{E}}{\vec{T}}{\boldsymbol{B}}^{+}$ to be linearly independent.  Describe yoUI' results in wonk  (c) \Yaves $\varLambda$ and $B$ (described respectively by ${\dot{E}}{\dot{\tau}}{\bf{\Omega}}^{+}$ and ${\dot{I}}\dot{\langle}r{\hbar}^{+}$ ) arc said t o  be ort hogonal in t he time domain if the instantaneous Jlower density carried by waws $\therefore$ and $_{\textit{13}}$ together equals the sum of the power densitips of t he individual waves.  IYhat restrictions must be imposed on $\dot{E}\tau{{A}^{+}}$ and $E T B^{+}$ if the two waycs are to be orthogonal in the time domain?  State your result in wonk  (d) Express the rpstrict ions found in (c) in terms of the components $E_{1}{}^{+}$ and ${\boldsymbol{E}}_{2}{}^{+}$ of $\chi_{T,\mathbf{i}}+$ and ${\dot{E}}{\dot{T}}{B}^{+}$ , and interpret the results for all possible circumstances rpgarding ${\boldsymbol{E}}_{1}{}^{+}$ and ${\vec{E}}_{2}{}^{+}$ .  

Problem 7.4.  Thc components of the complex electric field of a uniform plane wave propagating in the $+z$ direction are $\mathrm{l\!:}_{x0}^{}^{}+=\mid\!\mathrm{E}_{x0}^{}+\mid e^{j\vartheta_{x}},\,\,\mathrm{F}_{y0}^{}{}^{+}=\mid\!\mathrm{I\!:}_{y0}^{}+\mid e^{j\vartheta_{y}},$ (a) Show that the locus in time of the tip of the electric field vector satisfies the equation  

$$
\begin{array}{r}{\Big(\frac{E_{x}^{~+}}{|\mathrm{E}_{x0}^{~+}|}\Big)^{2}-2\,\frac{E_{x}^{~+}E_{y}^{~+}}{|\mathrm{E}_{x0}^{~+}|\,|\mathrm{\DeltaE}_{y0}^{~+}|}\,\cos\,\delta+\Big(\frac{E_{y}^{~+}}{|\mathrm{E}_{y0}^{~+}|}\Big)^{2}=\,\sin^{2}\delta}\end{array}
$$  

where $\pmb{\delta}=\pmb{\vartheta_{y}}-\pmb{\vartheta_{z}}$ ,  (b) Show that the coordinate axes, which in general do not  

coincide with the principal axes of the ellipse ootained above, can oe orought into coincidence with them oy a rotation aoout the z-axco through an angle $\boldsymbol{\varphi}$ where  

$$
\tan2\varphi={\frac{2\,|\,\mathrm{E}_{x0}{}^{+}|\,|\,\mathrm{E}_{y0}{}^{+}|}{|\,\mathrm{E}_{x0}{}^{+}|^{2}-|\,\mathrm{E}_{y0}{}^{+}|^{2}}}\cos\,\delta
$$  

(c) Under what condit iono dol's the ellipsc ,kgencrate into a straight line?  It circle? (d) A uniform metho(j of describing the sense in which the $\pmb{\cal E}$ -vector traces out the polarization ellipse has not been adopted in the scientific litcrature.  The most common pract ice is to view tbe fields looking in the dircction opposite to the (lirec­ tion of propagation, Le., in the negative $^z$ direction here, and then describe the polarization as being " right-han(lcd" or " left-handed," ,kpending on whether it is clockll"isc or countcrclockwise respectively in this view.  Under what analytical conditions is the polarization right-handed'?  

Problem 7.5.  The components in the $\pmb{x}$ , $y$ -plane of  the complex electric field of a plane wave are $\mathrm{{{J}}}\mathrm{{;}}$ and $\mathrm{I}_{\cdot y}^{\cdot}$ .  The complex ratio $\mathrm{I}\mathrm{?}_{E}=\mathrm{F}\mathrm{?}_{y}/\mathrm{F}\mathrm{?}_{x},$ , which can be repre­ sented as a point in a complex plane, determines the polarization in the $x,\,y\cdot$ -plane. In other words, each point of what may be called the H-plane has associated with it a differcnt clliptic polarization.  (a) l'rt'pare a sketch of the It-plane in which at rcpresentative points (e.g., points on the unit, $\ddagger\mathsection$ and 2 cireles which intersect the axes and the $\mathbf{45^{\circ}}$ lines) a small ellipoc i  drawn sitOlring (roughly) the inclination and relative ratio of the axes of the polarization ellipse as well as the direction of rotation about the ellipse.  Sec l'roh. 7.-1.  (b) If the $\mathrm{I}\dot{\boldsymbol{z}}_{x}$ and $\mathrm{F}_{\psi}$ are components of a uniform plane wave propagat ing in the $+z$ direction, what i  the rat io $13\pi$ of the complex magnetic field components in terms of $13c^{\circ}$ !  Descrihe how the diagram constructe(l in (a) can be use(1 to ohtain the polarization ellipse of the magnetic field corresponding to a given polarization of the electric field.  (c) $\mathbf{\Phi}_{\lambda}$ certain medium has the characteristic that it propagates plane waves in pairs, such that to each wave with polarization in the $x,\,y$ -plane described by the ratio $1\!\!\uparrow\!\!\varepsilon\!\!\!\mid$ corresponds another \\'ave with ratio $\mathrm{R}_{E2}\,=\,1/\mathrm{I}\!\left(\lambda_{E1}\right.$ .  Describe how the sketch preparcd in (a) can oe used to relate the polarizat ions of cOlTespomling ,,·aves.  

Problem 7.6.'  Two statistically ill<iPpeIHlent noise voltages, each of zero mean value, are applie(j respectively to the horizontal and vertical plates of an oscillo­ scope.  (a) Sketch one of the patt crm that might be traced on the scope face in a short observation interval.  (b) Suppose that the two noise voltages have equal nns values allll that each i  charactprize(i by a Gaussian amplitude distribution. Show that, if these voltages arc regarded aei the $_x$ ami $y$ components of tbe electric field of a uniform plane wa vt', this \I'a ve will be " randomly" polarized, as defined in the text.  (e) Is t he polarization still " random" if the two noise voltages are Gaussian, but have diffel'('nt rms values'!  Explain.  (d) Let the prohability den­ sities of the t\\'o noi,se voltages be $p(\boldsymbol{x})$ and $q(y)$ respectively.  Find all pairs of densities $[p,q]$ such that the polarization of the uniform plane wave discussed in (b) is " random."  

Problem 7.7.  The complex electric field vector of an electromagnetic wave in free space (vacuum) is given by the expression $\mathbf{E}\,=\,10^{-4}(a_{x}\,-\,j\alpha_{\iota\iota})e^{-j:0\pi z}\,\mathbf{v}/\mathbf{m},$ .  (a) Find the frequency $\pmb{f}$ .  (b) Sketch the instantaneous electric field vector $\tilde{E}(t,z)$ at $\boldsymbol{z}\,=\,0$ ,  

1 This problem requires a little familiarity with the principles of probability and statistics.  

showinl!; on a ;;inp;le (Iiagram it  map;nit lllle and orientation at t imes $\boldsymbol{t}=0$ , $\smash{t=1/\!\!\:1\!\!\:}$ , $t=1/2f,$ , awl $t\,=\,3/{\cdot}1\,\!\int$ .  (e) ItC'pcat (b)  at $z\,=\,0.025\,\mathrm{~m~}$ .  (d) \\"lw.t i  the typc of polariza t ion of the wave?  (e) Find t he cOlllplex mal!;nctic field II.  (f) Hepcat (b) and (c) for t he instantancou  magnet ic fielll vector $\pmb{\cal U}(t,z)$ . $\mathbf{\rho}(\mathbf{g})$ Find the complex l'oyntinp; ,"eetor $\mathbf{s}$ and the inst:mtaneous Poynting vector $s$ for the wave.  

Problem 7.S.  Given the following complex amplitude for a sinusoidal electric field in a  vacuum $\mathrm{~E~}=\,10(a_{x}+j0.4a_{y}+j0.3a_{z})c^{+j0.6y}c^{-j0.8z}$ .  (a)  \\"hat kind of disturhance is n'prl'spntcd hy thi  field and what b its frequency'?  (b) \\'hat is its direction of propap;at ion'?  (c) \\"hat is its state of polarization'?  Explain.  (d) Find the associated magnctic field.  (e)  Find the average power flow per square meter lIormal to the direction of propagation.  

Problem 7.9.  A t ravelin p; uniforlll plane wave propal!;atps in air in a direction mak­ ing equal acute ang!cs wit h the $+x-,+y-,$ and $+z$ -axes.  The electric field vector lies at all t iIlles in a plane parallel  to the $x,\,y\cdot$ -plane, and at $x\,=\,y\,=\,z\,=\,0$ has a map;nitudc, $|\,E_{1}(0,\,0,\,0,\,t)\,|=f(t)$ .  (a)  Express analytically the electric and  mag­ netic fielcl , $\dot{I_{21}}(x,\,y,\,z,\,t)$ and $\pmb{I}\pmb{I}_{1}(x,\,y,\,z,\,t)$ , of the wave.  (1)) EXJ>rc   analytically t he clectric and map;netic liehls, $E_{:}(.,\,y,\,z,\,t)$ and $I I_{\mathbb{2}}(x,\,y,\,z,\,t)$ , of a second travrling uniform plane wave that i  propagating in the same dircction as wave 1 ,  has $|\,E_{2}(0,$ $0,0,\ell)\,|=f(\ell)$ , but i8 orthogonal to wave 1 .  

Problem 7.10. $\therefore$ uniform planc wave i s  moving i n  the Z direction with $E=\,a_{z}100$ $\sin{(\omega t-\beta z)}+a_{i}200\cos{(\omega t-\beta z)}$ .  (a) EXJ>rcs $\pmb{U}$ by use of :\Iaxwcll's equations. (b)  I f  the W:lve PJl('outltcrs a perfect ly cond uct ing; $x,\;y$ -pl:lIlc at $z\,=\,0$ , cXlll'e,'s the I'csultinp; $\chi$ a nd $\pmb{\mu}$ for $z<0$ .  (c) Find the magnitude and direction of the surface (,l1I'rcnt density on the l'l'rfeet conductor.  

Problem 7.1 1 .   A uniform plane "'avc in free space st rikes normally a semi-infinite slah of lo,..;sIess materi:t l .   I n  the fr('e space, t he st anding wave rat io is 3.  In t he material, t he wave l('np;t h is shortcr by a fad or of (j t han it is in frcc space.  Find the relative permeability $\mu/\mu_{0}$ and rcla tive permittivity $\epsilon/\epsilon_{0}$ of the material .  

Problem 7.1 2. $\mathbf{\Phi}_{\lambda}$ uniform plane wave, $f=3.75\,\times10^{7}\,\mathrm{c}_{\mathrm{[}}\mathrm{)}\mathrm{s},x\cdot$ -polarized, strikcs nor­ mally a slab of lossless dielectric l "lckcd by a pcrfcct ly eonductinp; layer.  The di­ elect ric has $\epsilon/\epsilon_{0}=\cdot1$ and is $1.0\;\mathfrak{n}\mathfrak{\tau}$ thiek.  (a) \\"hat is $\bar{\mathbf{I}}$ at t he air-dielectric interface'? (b)   k(,t ('h to seale t he alllplit udes $|\operatorname{l}\rangle_{\!\varepsilon}|$ and $|\,\Im\,[_{y}\,]$ as functions of $^z$ outside awl inside the di('lcetric.  (c)  I f  the t hickncs,.; of the dielcctric is $2.0\,\mathrm{\Omegam},$ , what change occurs in (b)?  

Problem 7.1 3.  (a) Fillli thc th rce 1011"Cst frequ(,llcies at ,,·!tieh all thc inddcnt power ill Fig, 7.37 will be transmitted.  The permeability of all mcllia is $\pmb{\mu}_{0}$ .  (b) If complete transmission is required for a llY t hickness of the center medium, what is the lowest usable frequency?  (e) For the situation shown in the fi!,;1ll'e, find the banlhddth of the t ransmission l)ctw('cn its two lo\\'cst pelTcnl :lge yalucs adjaC'cnt to and on either side of the frequency of (b).  Find also these luwest perecntage values of the transmission.  (d) \rhy dol'S the reflection from the modern coated optical lenses telH! to be purple in color?  

![](images/fd49ff393dc34a8ea61dc24660a0874c79fdb04ddcfd3828a861ce0d18717c06.jpg)  
F i g .  7.37.  Problem 7.13.  

Problem 7.14.  A slab of lossle s dicll'ct ric has constant parameters $\epsilon_{1},\ \mu_{1},$ ,  awl t hickncss I.  It is intcrposc(l nOl'mal to the dircct ioll of pro]>ag,d ioll of a uniform plane waye in free spaee.  (:t)  kct ch t he t r:lIlsmission-lill<' an:t!o!,; of the systcm. (ll)  kpt ch t he t ransmissioll dlicipncy of t he shpet V<'rsus its thickness measured in In'(' SI)(l('c wave It'n!';t hs.  Take $\mu_{1}=\mu_{0}$ and $\epsilon_{1}=2.25\epsilon_{0}$ as an example.  Sk(,teh on t he same axes t he refiee-t ion dlicit'IH'Y.  (e) ( 'ndt'r what. cOlldit ions $(()\mathfrak{n}\ \epsilon_{1},\ \mu_{1},\ \tilde{l}_{z}$ , and t he fn'f1ut'ney)  dOl'S the slab l lphave \\'it h respl'c1. to point s out side it like a itlmlH'd capacitor shunt t'(! across a frec-space t ransmission line'!  (d) The n'sult.s of (a) su!';!';pst t hat a pane of window !';lass (for \\,hich $\epsilon\cong2.25\epsilon_{0}$ ttt opt ical frequencies) ('an dist ort the color of a s('clle vic\\'pd t hrough it, :lIIcl, part iculariy, of a scene rcflpct cd in it !  Why i  thi  sugg('st ion false'?  Cakulat e t he lllllnb('r of maxima of t h(' transmission or rdl('et ion r[[icil'n('y of :t $\xi_{\cdot}$ -iJl . ,h(,pt of gbss for normal incidelH e in the wave-ll'llgt h  ran!';e of yisible light. $(\downarrow\times10^{-7}\mathrm{\,m\,<\lambda_{0}\,<7\,\times10^{-7}\mathrm{\,m}})$ .  (e) :'.Iake a rough cst imate of t he t hiekllPss of a film of oil float ing OIl \\'at pl' if parts of the film appeal' 1,Iue and part s appear rpd \\'hclI \·ic\ypd wit h r(,(leet cd li!';ht..  The opt ical propert ips of t he oi l a l'e rou!';hl,r t he samc as those of t he \yilldo\\' glass.  

Problem 7.1 S.  (a) A paralkl-fac'cd slah of dieJpct ric  (medium $\boldsymbol{I},$ ) of t hickncss $\iota$ RP(lamtes t \\'o difTen'nt dipJp et ric n'!,;iolls (mcdia $\pmb{\Omega}$ and $c$ ) .  Calculate the squared magnitude of the refleetion cocllicipnt, $|\bar{\Gamma}_{12}|^{2}$ , for a mon(whromat ic uniform plane wave at normal incidence from medium $\pmb{a}$ ,  Assume t here is no refleeted wave in medium c.  Express your result. in t crllls of $\Gamma_{1},$ the reflection codlicient that would apply at boull<lary 1 betwccn media $^{a}$ and $l,$ if this w('re the only boundary in existence, and $\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}\mathbf{\Gamma}$ the corrcspondin!'; reflee( ion coeflieipnt at boundary 2 betw('en medi:L $\textit{b}$ ane! $c$ .  Int crpret $1-|\bar{\Gamma}_{12}|^{2}$ physically.  (b) $\cdot^{\backprime}$ source of bl'O:vlbalH! visihle li!';ht, whose continuous p(J\\'('r dpnsity 'ppe( rulll is fairly flat o\,pr many periods of t he fUl}('t ioll $|\bar{\Gamma}_{12}|^{2}$ found abo\'(', illumill:d ('s t he slab . .\s suming t hat. t he eye or ot.her opt iral inst rUnH'llt rpsponds to the nl('an 'quare value of t he rcfl('ct e(1 fipld st rPll!';t h,  deduee t he  opt ieal  rdl('et ioll pllici('ncy $\langle\,|\,\overline{{\Gamma}}_{12}|^{2}\rangle$ of t he slab t hus !llpas­ med.  Exprcss t he anS\\'('1' in t ('rllls of para lllct prs $g_{1}=\mathrm{\Delta}\Gamma_{1}^{\mathrm{~\cdot~}2}$ and $g_{2}=\Gamma_{2}^{\prime}{}^{2}$ .  (e) Derive the result of (I l) by adding up the ]iIJII'IT8 of the various mult iply r('fl('ct ed com­ ponellts  of  the  composite reflee(ed  wave.  Call'ulat e  t hc  opt ieal  tmnsmission cIlicielley of the doulJle boundary in the same way.  (d) Optically, in "ituations like that discussed above, n parallel shcets of gla,s separat ed by ail' eOllstitute $2n$ equally reflecting uoundarics in cascade.  The sheet thieknesse;; and spacings are irrelevant.  From your result of (Il), calc ulate the optical tmnsmission and re­ flection efliciencies at normal incidellce of such a multiple boundary.  

Problem 7.16. $\therefore$ dielectric slab (mediulll 2 of Fig. $7.38a$ ) cxtends over the entire x, $y_{}.$ -plane.  The system between t.he " input" and " out put"  p!an('s is t o  be rpg:mlcd as a filt er whose inst ant aneous input and out put funct iolls arc $k_{x i}$ and $k_{z o}$ respC'c­ t ively.  The filtpr illput is a norlllally incident uniform pl:l1lc wave.  (a) For $\epsilon_{2}=$ $36\,\epsilon_{0}$ , filUl t he impul,-;e respollse of t he s),st pm.  (b) It is desirp(l to modify the fiI t pr so that it has the nel\' impulse response shown in Fig. $7.38/\rangle$ >, in which $\angle1$ can be any positive constant and $T_{0}=\%\times10^{-8}$ scc.  The time interval between $\scriptstyle t\;=\;0$ and the first output impulse is of no concern.  Find the thickness $d$ and the permittivity $\pmb{\epsilon2}$ of the dielectric slab required to obtain the desired impulse response.  

![](images/3d7bb34b29e23f05cad135f9e0f2c51e5e4034bd1549cb6423b24b174e1f1f47.jpg)  
F i g .  7.3 8.  Problem 7.16.  

Problem 7.17.  In the sinusoidal steady state at frequency w, a linearly polurized uniform plane wave is incident at angle $\vartheta$ upon a perfect conductor whose surface dcfines the $_{\pmb{x}}$ , $\mathcal{Y}$ -plane.  The incident magnetic field is parallel to the conductor, and has an amplitude $I I_{0}$ which it attains in the $+x$ direction at $x\,=\,y\,=\,z\,=\,t\,=\,0$ . (a) 'Yrite expressions for the complex-vector electric and magnetic fields ${\bf E}_{i}(x,\,y,\,z)$ and ${\mathbf{I}}{\mathbf{I}}_{i}(x,\,y,\,z)$ of the incident wave.  (b) "'rite expressions for the complex-vector electric and magnetic fields ${\bf E}(x,\,y,\,z)$ and ${\mathbf I}{\mathbf I}(x,\,y,\,z)$ of the complete field solution to the problem.  (c) "'rite the expression for the real instantaneous surface current density vector $\bar{\kappa(x,y,t)}\,\,\mathrm{amp/m}$ on the metal.  (d) Write the expression for the real instantaneous surface-charge density $Q_{s}(x,y,t)$ coulombs/ $\mathrm{\vec{m}}^{\bar{2}}$ on the metal. (e) Repeat for a circularly polarized incident wave for which $I I(0,0,0,0)\,=\,a_{x}I I_{0}$ . (f) For the case (e) , when $\vartheta\,=\,0$ , determine the instantaneous and complex Poynting vectors, $S(x,\,y,\,z,\,t)$ and $\mathbf{S}(x,\,y,\,z)$ respectively, and interpret them.  

Problem 7.1 8.  A uniform plune wave is incident at angle $\vartheta_{1}$ upon the interface between two lossless dielectrics.  The (real) angle of refraction is $\vartheta_{2}$ .  'Vhen the polurization is parallel to the interface, the reflection coefficient is $^{1\!}$ .  (a) Find the numerical value of the transmission coefficient.  (b) If the propagation direction of the transmitted wave is reversed, thus making this wave become a new incident wave with the same polarization as before, what will be the numerical values of the reflection and transmission coefficients?  (c) If $\vartheta_{1}=60^{\circ}$ and $\vartheta_{2}=30^{\circ}$ above, repeat (a) and (ll) for these same values of $\vartheta_{1,2,}$ but with the polari7.ation rotated $90^{\circ}$ .  

Problem 7.1 9.  A uniform plane wave of frequency w polari7.cd in the plane of incidence is obliquely incident at angle $\vartheta$ from air onto a loss less dielectric with $\mu=\mu_{0}$ and $\epsilon>\epsilon_{0}$ .  l\feasurement of standing wave ratio $\pmb{\bar{s}}$ is made with a probe sensitive only to tangential components of electric field, and moving normal to the interfaces, for the following two cases : Case 1- $\vartheta=30^{\circ}$ , $\pmb{\mathscr{s}}=\pmb{\mathscr{s}}_{1};$ ; $C a s e\;\mathcal{Z}{-}\vartheta=45^{\circ},$ , $\mathbf{s}=s_{2}$ .  It is found that $s_{2}/s_{1}=\mathbb{\tilde{\gamma}}_{3}$ ]i.  Find :  (a)  The specific permittivity $\epsilon/\epsilon_{0}$ . (b) The value of $\pmb{\mathscr{s}}_{1}$ .  

Problem 7.20.  (a) A flat plastic platc $(\epsilon/\epsilon_{0}\,=\,2.25)$ is 2 in. thick.  A uniform-plane electromagnetic wave of frequency $10\,\mathrm{\kmc}$ is incident on the plate at an angle $\vartheta_{1}$ (from the normal) .  The polarization is parallel to the surface.  Find all values of the angle $\vartheta_{1}$ for which reflections are eliminated.  (b) Hepeat part (a) with the wave polarized in the plane of incidence.  

Problem 7.21 .  An experiment is being de igned to illu trate clearly I3re\\'ster's angle for a givcn plast ic $[(\epsilon/\epsilon_{0})\,=\,2.25$ , $\mu\,=\,\mu_{0}$ , $\sigma\,=\,0$ ].  The method consists of measuring uirectly the reflected uniform pbne wave fielu from a sheet of the material, as a function of incident anglc, at a microwave frequency $f=10\ \mathrm{kmc}$ . The plastic is very expensive, so minimum thickness is desirablc.  On the other hand, if the reflections are never very stron!!; at any angle, the sensitivity of the null is poor.  There is abo the problem of avoiding " false" nulls (sec Prob. 7.20) within the angle range considered practical (say, $0^{\circ}{-}85^{\circ},$ ) .  (a) Determine reasonable limits upon the thickness of the plastic sheet.  (b) Dbcuss the efTect upon the experiment if the incident plane wave source actually emits a pencil of waves with uirections lying in a cone of small half-angle $_{\alpha}$ rad, and if the rcceiver for the reflected wave can be twisted about its O\\'n axis by $\pm\alpha$ without changing its indication of a given uniform pbne wave directed at it (twisting by more than $\pm\alpha$ rad gives zero indi­ cation) .  Consicler the relationships between the transverse sheet dimensions anu the distances between source, sheet, and receiver.  Comment also on what factors fix the angle range usable in the experiment.  

Problem 7.22.  A plane wave which in air ha  a $10~\mathrm{{cm}}$ wavc lcngth is incident on an air-dielectric interface from the dielectric side.  The permeability of the dielectric is equal to that of air, and $\epsilon_{1}\,=\,4\,\epsilon_{0}$ .  (a) What is the critical angle for no transmitted power into the air?  (b) A nonmagnetic coating is to be added to the dielectric to make the interface nonreflecting at normal incidence, again from the dielectric side. \Yhat thickness $\boldsymbol{a}$ and dielectric constant '2 should this coating have?  (c) Hepcat (a) with the coating determined ill (b) in place.  

Problem 7.23.  Prove or disprove : There is always one and only one angle of in­ cidence of a randomly polarized uniform plane wave on a boundary between two lossless media, characterized by constant parameters $(\epsilon_{1},\,\mu_{1})$ and $(\epsilon_{2},\,\mu_{2})$ , at which the reflected wave is linearly polarized.  (Culition: Bear in mind tlmt if the angle of incidence exceeds the crit ical angle, the incident wave is totally reflected.) Hehte the polarization of the reflected wave to the parameters of the two media for those cases in which the reflected wave is linearly polarized.  

Problem 7.24.  The boundary between t\\-O lossless dielectrics is the plane $z=0$ . The wave impedance and speed of light in the left-hand $(z<0)$ dielectric are $\pmb{\eta_{1}}$ and $v_{1}$ ; in the right-hand dielectric these quantities are $\pmb{\eta}2$ and $\pmb{v_{2}}$ respectively.  A tra veling wave having the electric field  

$$
E_{i}=a_{z}f\bigg(t+\frac{y\sin\vartheta_{1}-z\cos\vartheta_{1}}{v_{1}}\bigg)\quad\;\;z\leq0
$$  

is incident on the boundary from the left.  (a) Express both electric and mal!;nctic  

# 3 98  ELECTROMAGNETIC ENERGY TRANSMISSION AND RADIATION  

fields of the incident, reflected, and transmitted waves if $\vartheta_{1}$ is less than the critieal angle.  (b) Let $f(\tau)$ be the rectangular pulse  

$$
f(\tau)\;=\;\Big\{\!\!\begin{array}{l l}{{1,}}&{{\quad|\tau|\leq\frac{1}{2}}}\\ {{0,}}&{{\quad|\tau|>\frac{1}{2}}}\end{array}\!\!
$$  

ami let $\vartheta_{1}=60^{\circ}$ , $\boldsymbol{\tau}_{2}=\dag;\boldsymbol{2}v_{1},$ , alll i $\eta_{2}=\eta_{1}$ .  I::iketch allli  dimension the contours in the $y.$ , z-plane: amplitude of total electric field $=$ constant.  :\ I ake your contour "map" at the instant $\ell=0$ , antI indicate with arrows how these contours change as time ad vances.  (c)  Xow buppose $v_{2}>v_{1},$ , and t he angle of incidence exceeds the critical angle.  The c1eelric licltl of the incidcnt traveling wave is expressed in terIllS of the Fourier t ra nsforIn $\mathrm{I}^{*}(\omega)$ of the fUlldion $\textstyle{f(\tau)}$ :  

or  

$$
\begin{array}{l}{{E_{i}=\displaystyle\frac{1}{2\pi}\int_{-\infty}^{+\infty}\!\!\!\alpha_{x}\mathrm{F}(\omega)e^{j\omega\{t+[(y\sin\vartheta_{1}-z\cos\vartheta_{1})/v_{1}]\}}\,d\omega}}\\ {{\displaystyle E_{i}=\displaystyle\frac{1}{2\pi}\int_{0}^{+\infty}\!\!\!2\,\mathrm{Re}\,[a_{x}\mathrm{F}(\omega)e^{j\omega\{t+[(y\sin\vartheta_{1}-z\cos\vartheta_{1})/v_{1}]\}}]\,d\omega}}\end{array}
$$  

since $E_{i}$ is a real wetor.  Express similarly both the elcetric and magnetic fields of the reflected and t r:msmitt etl waves,  (d) If you had u,-;ed the first given form in amwcring (e),  lI'ould your t raw'lllission and reflcct ion cocflicicnts depend on frequency'?  I I olI" ?  \\' hal if you had u:ictl the second given form'?  \Yklt auout the coeflicicni of z,  COlTcsl 'owlillg to $-\cos\vartheta_{1}/v_{1}$ above,  i n  the expressions  for  the transmitted fields'?  Find t\\'O dijJ('J"cnt argulllcnt s to support your answers to these quest ions,  (e)  Let $\scriptstyle{f(\tau)}$ hc a  unit impulse at $\tau\,=\,0$ ,  From your ans\\"er to (e), calculat e, by aetu:dly performing t.he int egration , the electric field in the $\boldsymbol{x}$ , z-plane on the right of t he boundary,  ] )oes your calculation sho\\"  thi  field to be zero uefore the arrival of the inci,!cnt wave at the origin'?  Explain,  

Problem 7.25 .  COll id('r :\[axII'cll"s cquat ion  for a los lcss source-free regioll with cOllst ant permi t tivity € alltl permeability $\pmb{\mu}$ l.  (a) Show that the rectangular vector componellts of t he st eady-stat e complex electric fielt! E obey the equation $\nabla^{2}\mathbf{E}+\mathbf{\Psi}$ $k^{2}\mathbf{F}=0$ $(k\,=\,\omega\sqrt{\epsilon\mu})$ and that I I  olJP)"s the same equat ion.  (b) Cndel' what con­ dit ions on the complex cOlls(,mts $\bar{\gamma}_{\bar{\tau}},\;\bar{\gamma}_{1/\nu}$ and $\bar{\gamma}_{z}$ i $\mathbf{E}(x,\,y,\,z)\,=\,\mathbf{E}_{0}e^{-(\bar{\gamma}_{x}z+\bar{\gamma}_{y}y+\bar{\gamma}_{z}z)}\,\mathbf{\sigma}_{\Omega}$ solution  to  the equation  in  (a) ,  \\'ith $\mathbf{E}_{0}$ a constant complex vector?  

Problem 7.26.  The complex fidd  produce(1 in a certain isotropic, homogeneous, linear,  time-invariant,  source-free  medium  by  a  1 00-me  sinusoidal  source  are  

$$
\begin{array}{r l}&{{\bf E}=\mathrm{I}_{0,c}a_{x}-20\pi[(13-j\!\cdot\!\bar{5})a_{y}+(26+j\!\cdot\!\bar{6})a_{z}]e^{-\pi[(1+j\!\cdot\!\bar{5})x-(3+j\!)y+(4-j\!)z]}}\\ &{{\bf H}=(\mathrm{II}_{0,c}a_{x}+\mathrm{II}_{0_{y}a_{y}}+\mathrm{II}_{0z}a_{z})e^{-\pi[(1+j\!\cdot\!\bar{5})x-(3+j\!)y+(4-j\!\cdot\!\bar{2})z]}}\end{array}
$$  

alld it i  kllO\\'1l that $|\,\mathrm{I}\,\mathrm{I}_{0z}\,|=7.$ (a) \Yhat can be said about t he mediuIll from the space varialion of t he fieltl '!  (b) \\"here i  the source'?  (Jive a ullit vector normal to a piane which sl'parate  a region ill space where the fidtls are bounrlcd from one where the fields are arbitrarily large.  Let the unit vector point to\nml the strollg­ field region.  (e) ])etermine  the Ull ])('cifiCtl field componenb, $\mathrm{I};_{0x},\ \mathrm{II}_{0x},\ \mathrm{II}_{0y},$ and $\mathrm{{II}}_{0;}$ .  (d) \Yhat arc the conduct ivi!y, rela! in  ]>('rmeability, ancl dielcctrie con tant of the medium'?  (c) Dcs('f"iile the fiPl"s in \\"()/'tk  Exactly what kintl of wave do they re]lre cnt?  (f) l Determinc the (eompkx) polar angles $\bar{\mathfrak{d}}$ and $\overline{{\varphi}}$ of the direction of propagation of the equivalent uniform planc wave,  

I The considerable algebra required for this part should be done carefully or not at all.  

Problem 7.27.  ,\ DOO-me nolltllliforlll TE plane wave propagates in air in such a malJncr t hat ib pha'c ilU'I'cascs most rapidly with position in a direction para l lel to, and lying in t he first quadrant of, t he $x,y\cdot$ f-plane.  The amplitude of the $\boldsymbol{x}$ -compo­ ncnt of the eledric field i, $3\ \mathrm{v/n}$ throughout the plane $x\,-\,2\,\!\langle\!\langle}~+\,2z\,=\,0_{\!\array}$ ; in the plane $x\,-\,2\,y\,+\,2z\,=\,1\,/\,\pi\,\,\mathrm{{n}}_{,}$ ,  it  is $3c\ \mathrm{v/n}\mathrm{{}}$ .  (a) Determine the (complex) propa­ gat ion vect or of t he wave.  (b) Express the mo"t general field:; that fit the problem statl'nll'nt.  (0) ::iltow t hat the complex pobr  lJIgles for the direction of propagation of the equi valent uniform plane wave are $\bar{\vartheta}\,=\,\pi/2\,-\,j\sinh^{-1}\,\bar{\slash}\,\bar{3}$ and $\overline{{\psi}}\,=\,\tan^{-1}$ $\smash{\downarrow_{2}^{\prime}+j\operatorname{tunh}^{-1}\downarrow_{3}^{\prime}}$ , \\'ith  He $(\vec{\varphi})$ in the third (J lwdrant.  Do not use a ;,;lide rule or tables.  

Problem 7.28.  Consider fields of t he form $E=\mathrm{l}\mathrm{i}\mathrm{e}\ \{\mathrm{E}e^{-\{:i t}\}$ , $\mathbf{E}=\mathbf{E}_{0}e^{-{\bar{\mathbf{Y}}}\cdot\bar{\mathbf{r}}},$ , $\pmb{\mathscr{M}}=$ Ill' $\{\mathbf{\Delta}\mathbf{I}\mathbf{I}\boldsymbol{\epsilon}^{-:\iota}\}$ , $\mathfrak{u l}=\mathfrak{l}\mathfrak{l}_{0}\mathfrak{c}^{-}\bar{\mathfrak{v}}\cdot\pmb{r}$ in  a  los"ll'''" medium  Il'ith $\Omega$ a. pure real number all $\mathbf{{F}}_{t_{1},\mathrm{~\tiny~\textnormal~{~\textcent~}~}}\mathbf{{I}}_{0}$ COIllpll'X vcctors.  (a)  I f  t hl'se fields are  to  satisfy  :\ !axwcll'>j equations, Il'hat con"t rainh Illust I ,e illl! ,o", d on $\mathbf{I}_{00}$ , $\mathbf{l}\,\mathbf{I}_{0}$ , allLl "F  On $\mathbf{\tilde{f}}_{0}$ and 'I'!  On $\mathbf{II}_{0}$ amI ${\bar{\mathsf{Y}}}?$ On 'I a lou,,'?  (IJ) Expn'''s $\varepsilon$ and $\pmb{U}$ i n  t he ease $\tilde{\gamma}_{x}\,=\,\tilde{\gamma}_{y}\,=\,\mathrm{l};_{0y}\,=\,\mathrm{l};_{0z}\,=\,0$ .  Describe th"se field,-; in lI'ords.  I fow could they be excited?  Could a " uniform plane wave source"  be u,-;c(l'?  (c)  Exami nc $\pmb{\chi}_{\pm}^{*}$ anll $\pmb{U}$ in the lIlore gcneral ('ase, $\bar{\mathfrak{Y}}=\mathfrak{a}+\mathfrak{j}\mathfrak{\beta}$ 3. lnt prr('late $\pmb{\upalpha}$ awl $\upbeta$ .  ])e ('ribe t hese ficld  in \\·onls.  How could tbey be excited ? (Ililll: :-Jtudy S('c. 7.·1.3,)  

Problem 7.29.  As illustrat ed ill Fig. 7.3!l, tll'O perfedly conducting and infinites­ imally t hin  hcets in ail' forlll :L sell/ i-infi n i t e  pal'allel-plate wave guide, with mouth i n   t ile  pblle $\pmb{z}=0$ anll  idc   parallel  to tbe $y$ / , $^z$ -pbnc.  Two $y$ -polarized,  st cady-st ate uniform plane Il'aves (1 and 2) of equal strcnp;th are incident upon t he mouth of the p;uidc at angl"s $\vartheta$ sholl'n, alld tllcir separate rquiphase ourfaces of the same phase  intersect  in lilles  lying ill  the $y$ ,  z-plane. (a) If the \\'ave length A of the incidcnt waves is such t hat sin $\vartheta\,=\,\lambda/2a\,=\,\sqrt{3}/2$ and t he pcak fiehI st rength ill each is $1\,\mathrm{\Deltav/m}$ , filld the t ime-average powcr flOll'ing dOII·n the inside of the  guide,  pCI' metcr of tlte $y$ dimcllsion.  (b) Hcpcat (:1) if II·ave 2 is  tlll'lled ofT.  (e) H qwat (a) if mlve 2 is present IHlt reversed in time phase.  Check your result by veri fying the relat ionships bet ween t he ans\\"er  to (:1), (b), (c) by a  difTprent  method  than  the  one u"cd to get t hem.  (d) SU!'I)()se $\vartheta$ bas :L given arbi­ trary ]'('al value, not specially relate(l t o $\lambda$ , and we det ermine by nH'asurcnwlIt that power $\langle I^{\flat}\lrcorner1\rangle$ goes <10\\'11 the inside of the guide (pCI' met er of $y$ dimension) when wave 1 alone is inci­ dent at power density level $\langle S_{1}\rangle$ .  In terms of $\langle{I^{\flat}}_{\mathrel{\cdot}1}\rangle$ find : (i) The power down the guide if l\'aye 2 is turned on with $\langle S_{2}\rangle\,=\,\langle S_{1}\rangle$ und with identical phase at the origin; (ii) The result of (i)  if wa\'e 2 has revcr.,e([ time phase.  

![](images/6e9574d3980c77e1fd833ff6030ce959cf107add18a639348934d96029985de3.jpg)  
Fig. 7.39.  Problem 7.2\l.  

Problem 7.30. $\therefore$ long piece of $3{\mathrm{-cn}}1$ rectangular wuve guide (inside dimensions 0.4 in. $\times\:0.9$ in.) is filled with polystyrene blocks $(\epsilon=2.5\epsilon_{0})$ so that the $\mathrm{{^TI!}}_{1,0}$ mode will noll' propagate in the guide at $\mathbf{\Xi}_{\delta}\mathrm{~l:m~c~}$ ,  One end of the guide is connected to a matched load all(l the OtI1PI' to a 5-kmc source.  In assembliIlg the equipment, t \\'o of t he blocks a re spparatp(l so that t here is a rectangular air-filled sect ion of guide, Ita ving a Icugt.h l and located half\\'ay I,elll'ccn source alld load.  You are to determine fields and powcr flow in the vicinity of th e air gap.  (a) Show that only the $\mathrm{TI}\!\!\!\backslash\!\!\!\backslash\!\!\!\backslash\!\!\!\backslash\!\!\!\!\backslash\!\!\!\!\backslash\!\!\!\!\}.\!\!\!\!$ mo(le transverse pattern is needed to meet boundary conditions in cach of the three sections, and that the longit udinal parts of the problem may be solved by transmission-line analogy.  (b) The fiplds in t he air-filled section can be decompused into two waves-aile that decays exponentially with di:.;tance along the guide as it approaches the luad end of the section, and one that decays cxponen­ tially as it approaches t he source cnd.  lIow much mC'an power is carried toward the load by each of these waves s('parately?  Can any power reach the load w hen both arc present together'?  ( ce l'rob. 3.-Hl.)  (c) Caleulate the rat io of the total electric field in the center of the guide at the boundary of the air-filled sectiun nearcst the load to the corresponding quantity at the boundary ncarc:.;t the source. Show t hat the magnitude of this ratio does nut exceed 1.  (d) Caleulatc a1l<1 sketch, as a funct ion of $l_{:}$ the rat io of the load power to the power uf the source wave that is incident on the air-fille(1 section frum the dielcctric-filled one.  (e) Calculate the YS\YR, for $\ell=1$ in., in those sections of the gui,lc in ,,-hieh t he \" \rn cunccpt applies.  From t hese results, and those of (d), discu:.;s the eleet rical limitations to making out of thi:; device un atteIluator fur w hich loss in decibeb will be directly proportional to length l.  

Problem 7.3 1 .   Consi,ler a $\mathrm{TI}\mathrm{:}_{m,0}\;(+)$ -,,-ave in a luss]Pss reetanp;ular wave guide of wide dimension $a$ and narrow dimcn;.;iun $\upsilon$ .  Define " voltage" $\Upsilon_{+}$ as the line int egral of the electric field up t he center of t he cru:,s sC'el ion, alung a line paral lel to the narrow side.  Define current $\mathrm{I}_{+}$ s o  t hat $\mathrm{^{1}{^{\cdot}}\mathrm{^{\cdot}}\mathrm{^{\cdot}}\mathrm{^{\cdot}}\mathrm{^{\cdot}}\mathrm{^{\Sigma}+}}^{\Sigma}$ gives cOrIwtly the total complex power carried lungitudinally through the cross section (as determined from the complex Poynting wetur) .  (a) From the values of $\bar{\gamma}$ and ${\bf Z}_{0}\equiv\mathrm{Y}_{+}/{\bf I}_{+},$ , determine t he series impedance pCI' unit 1(,llgth $\mathrm{Z}_{s}$ and t he shullt udmittance pCI' unit length $\dot{\Upsilon}_{p}$ of an equivalent transmission line fur this mo(le.  (b) :'-Iake a circuit diagram repre:'enli ng a Icngt h $d z$ uf the line in (a) .  In this diagram ail cl('ment values must be ilic/l'IJCIuicnt of frc(juency.  How docs t he cutoff frequency show in the equivalent circuit?  (e) Identify the energy store,l in each elpment of the equivail'nt circuit with that stured in the act ual mode by one space component of t he electric or magnetic fiel,!.  (d)  If a difTcrcnt line intcgral is taken to define $\mathrm{V}_{+}{}^{\prime}$ , so t hat $\Upsilon_{+}^{\prime}\prime=$ $I\backslash^{\mathrm{\scriptscriptstyleT}}+_{\mathrm{1}}$ , but we still chuose ${\mathrm{I}}_{+}{'}$ such t hat $\mathrm{^{1}_{^{2}}V+^{\prime}I_{+}}^{\prime}\mathrm{^{*}}$ represents the COlTect cumplex power, reconsider your results in (a)-(c) _  (c) Coul,l I\e chuuse to define " vultage" proportiunal to t ransverse magnetic field and " cu rrcnt" propurtioJlal to transverse eleelric field 'I  Illustrate.  (f)  If we chose " current" proportiunal to longitudinal magnetic fi('I,I, what chuices arc open for " voltage"?  Hepcat if " vultage" is eho:;cn proportional to longit udinal field.  Illustrate.  

Problem 7.32.  I n  the rarefied upper atmo"'phC're several hundred kilometers above the earth's surface there exists a region of e1cnse, horizunt ally strat ified iunizat ion caused by solar radiation.  The several ionized layers are known collectively as the ionosphere.  The parameters of un ionospheric layer may be taken to be $\sigma\textbf{=}$ $0,\;\mu\,=\,\mu_{0},\;\epsilon\,=\,\epsilon_{0}[1\,-\,(\omega_{p}/\omega)^{2}],$ ,,·here $\omega_{p},$ the plasma frequcncy, is proportional to the square root of the electron density.  (a) Obtain the propagation constant $\overrightarrow{\mathbf{\xi}}$ and the wave impeelance $\bar{\pmb{\eta}}$ of a uniform plane wave in such an iunospheric layer. (b) A uniform plane l\'ave in air of electric fiel,l $E_{1}=a_{x}$ l e $[\mathbf{E}_{1}e^{j(\omega t-\beta_{\mathrm{0}}z)}]$ strikes a hypothetical abrupt boundary $z\,=\,0$ of un ionospheric layer from below.  Xeglcct ing reflect ions  frum the upper  boundary of the  layer,  express the t ransmitte<i and reflect ed fields in t he eases $\omega>\omega_{p}$ and $\omega<\omega_{p}$ _   kctch the square, I magnit ude uf the reflectiull cueflicicnt as a  fUllctiun uf frequency for $0\,<\omega<2\omega_{p}$ •  (The reflcct ion coefficient of an actual ionizcd layer which docs not have abrupt boundu" ics diminishcs much more rapidly with frcqucncy when $\omega>\omega_{p}$ ,)  (c) On a particular date and time of day, and above 11 particular geographical location, the dcnsest ionization occurs at an altitude of $\cdot400\ {\mathrm{km}}$ , and the plasma frequency of this dense ionization i $\omega_{p}/2\pi\,=\,5\,\mathrm{\m}$ c.  .l\cglccting ionization bclo\\' tltis densest layer,  de­ termine the greatest possible angle of incidence $\vartheta$ (Fig, 7.'10) at which radiation from ll.  ground-based transmitter could possibly strike the layer.  (d) lIo\\'  far ll.way from the transmitter will the reflected rtHliation return to earth?  (e) \Yhat is the highest frequency at which this ooIiquely incident radiation will oe totally reflected?  (f) A radar set is used t o  measure the dist ance to the moon at a time when the moon is at the zenith.  The hall<hl'idth of t he radar signal is small com­ pared with the difTerence hetwecn the ccnt er frcquency of the radar sil!;nal and the plasma frequency of the iono"phere.  Calcula t e  and sketch, a s  a function of the radar signal center frcqucncy, t he discrppancy hctween the mcasured and actual distances to the moon causc(l by passage of the radar signal through a uniforlllly dense layer of ionization $100\ \mathrm{km}$ thicl,- \,"hat range of crnter frcqupncics may he used if this discr('pancy is to bc less t han $1\ \mathrm{kn}?$ Xotc that the model of the iono­ sphere implied by the problem statement has alJl'upt bOUIHI:trif'H al1(1 thus woulel support multiple reflections of the t ransmitted signal and of the moon ('cho, both inside the ionized layer and bet\\·ccn its lower boundary and the earth.  For the purposes of this proolem, it may be supposed t hat t he mdar signal is a pulsed sinusoid of short enough duration so that the filA-arriving Illoon eeho  may  bc selected from the array of other eehoe.:; cau,sed by unwanted or Illultiple refl('ct ions.  

![](images/b665b3bdb17c7a06a7a00b86dcc74c4bc9f6ca9deb6aaf1154ff5f53d135de1f.jpg)  
Fig, 7.40.  Proolem 7.32.  