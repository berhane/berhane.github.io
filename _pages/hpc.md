---
layout: archive
title: "HPC"
permalink: /hpc/
author_profile: true
---

Advances in computer hardware and software algorithms over the recent decades has made computer modeling an essential component of research and discovery. Scientific modeling is now the third pillar of discovery alongside laboratory/field experiments and theory. While many modeling problems can be handeled by laptops, desktops and workstations, most rigorous computations require more sheer computational power, faster networking, larger storage, more memory, ... etc. When one's research workflow encounters limits associated with any of these problems with performance or throughput, it is time to look into high-performance computing (HPC) or high-throughput computing (HTC) capabilities to enable and accelate one's research.
 Over the last 10-15 years, the ability to build commodity HPC clusters from generic components and run free, open source software (FOSS) has made HPCs more affordable and it has expanded their use. The simplest way to think of HPCs is as a bunch of individual computers, often referred to as nodes, servers or blades, networked using a fast interconnect, equipped with fast shared storage, and packaged into a rack in such a way that they behave as a single, powerful computer.
 HPC resources and solutions are designed to have the following capabilities:

-   **Massive parallelism** - Many enterprise-grade servers and processors tightly coupled to enable parallel performance
-   **Large shared-memory nodes** - lots of memory on every node/blade
-   **Parallel file systems** - fast and reliable storage system
-   **Fast networking** - GigaBit ethernet and Infiniband/Omnipath fabrics interconnecting nodes/blades to one another and the shared storage system
-   **Efficient data movement tools** - commandline and GUI tools for quickly transferring data
-   **Visualization capabilities** - tools to visualize data on the HPC instead of having to transfer it to a remote host first

Many faculty at CofC do research that is computationally demanding enough to require an HPC resource. Some faculty already use HPC resources and we have identified many others whose work and workflow are good candidates for HPC/HTC. If you are interested in learning more about HPC/HTC at CofC, please email [me](mailto:temelsob@cofc.edu).
 To meet the HPC and HTC needs of researchers at CofC, we are working on three solutions.

-   **An HPC cluster on campus** - on top of a small cluster we currently have, we plan to acquire another cluster soon
-   **NSF XSEDE resources**- we have computer time at XSEDE resources and the expertise to help some users get started
-   **Commercial cloud providers** - we are exploring free/inexpensive options to use Amazon AWS, Google Cloud or Microsoft Azure for research purposes.

# New Campus HPC Cluster

Our new campus cluster has been installed in early March, 2019 and opened to a limited number of
beta testers in April, 2019. It will be open to all users starting April 22, 2019. <br>

Please learn more about the cluster and how you can get access by reviewing the
[documentation](<https://hpc.cofc.edu>). You can find a brief overview
[here](<https://hpc-cofc.gitbook.io/docs/using-the-hpc/overview>). Please send any questions about
the new cluster to [hpc@cofc.edu](<mailto:hpc@cofc.edu>). The cluster is accessable directly from
our campus network, but requires CofC's VPN for off-campus access.

# NSF XSEDE

`NSF XSEDE`[![NSF-XSEDE](<images/NSF-XSEDE.jpg>)](<https://portal.xsede.org/resource-monitor>)<br>

<br>

 National Science Foundation (NSF) provides an ecosystem of HPC systems across the country to support US-based researchers at no cost. Aside from the HPC systems, it provides personnel to help users get started and accelerate their research using XSEDE's resources. <br>

<iframe src="https://www.youtube.com/embed/PBUIBJHZzD4?rel=0&amp;controls=0&amp;showinfo=0" allow="autoplay; encrypted-media" allowfullscreen="" width="560" height="315" frameborder="0"></iframe>

<br>

  | Resource                                                             | Org                                                                  | Type                                                                 | Startup Allocation Limit                                             | User Guide                                                           |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| IU/TACC (Jetstream)                                                  | Indiana U                                                            | compute                                                              | 50000                                                                | [User Guide](<https://portal.xsede.org/jetstream>)                   |
| IU/TACC Storage (Jetstream Storage)                                  | Indiana U                                                            | storage                                                              | N/A                                                                  | [User Guide](<>)                                                     |
| LSU Cluster (superMIC)                                               | LSU CCT                                                              | compute                                                              | 50000                                                                | [User Guide](<https://portal.xsede.org/lsu-supermic>)                |
| Open Science Grid (OSG)                                              | OSG                                                                  | compute                                                              | 200000                                                               | [User Guide](<https://portal.xsede.org/OSG-User-Guide>)              |
| PSC Bridges GPU (Bridges GPU)                                        | PSC                                                                  | compute                                                              | 2500                                                                 | [User Guide](<https://portal.xsede.org/psc-bridges>)                 |
| PSC Large Memory Nodes (Bridges Large)                               | PSC                                                                  | compute                                                              | 1000                                                                 | [User Guide](<https://portal.xsede.org/psc-bridges>)                 |
| PSC Regular Memory (Bridges)                                         | PSC                                                                  | compute                                                              | 50000                                                                | [User Guide](<https://portal.xsede.org/psc-bridges>)                 |
| PSC Storage (Bridges Pylon)                                          | PSC                                                                  | storage                                                              | N/A                                                                  | [User Guide](<https://portal.xsede.org/psc-bridges#file-spaces>)     |
| SDSC Comet GPU Nodes (Comet GPU)                                     | SDSC                                                                 | compute                                                              | 2500                                                                 | [User Guide](<https://portal.xsede.org/sdsc-comet>)                  |
| SDSC Dell Cluster with Intel Haswell Processors (Comet)              | SDSC                                                                 | compute                                                              | 50000                                                                | [User Guide](<https://portal.xsede.org/sdsc-comet>)                  |
| SDSC Medium-term disk storage (Data Oasis)                           | SDSC                                                                 | storage                                                              | N/A                                                                  | [User Guide](<https://portal.xsede.org/sdsc-dataoasis>)              |
| Stanford University GPU Cluster (XStream)                            | Stanford U                                                           | compute                                                              | 5000                                                                 | [User Guide](<https://portal.xsede.org/stanford-xstream>)            |
| TACC Data Analytics System (Wrangler)                                | UT Austin                                                            | compute                                                              | 1000                                                                 | [User Guide](<http://portal.xsede.org/tacc-wrangler>)                |
| TACC Dell/Intel Knights Landing, Skylake System (Stampede2)          | TACC                                                                 | compute                                                              | 1600                                                                 | [User Guide](<https://portal.tacc.utexas.edu/user-guides/stampede2>) |
| TACC Long-term Storage (Wrangler Storage)                            | UT Austin                                                            | storage                                                              | N/A                                                                  | [User Guide](<http://portal.xsede.org/tacc-wrangler>)                |
| TACC Long-term tape Archival Storage (Ranch)                         | UT Austin                                                            | storage                                                              | N/A                                                                  | [User Guide](<https://portal.xsede.org/tacc-ranch>)                  |

 We have a small allocation at [NSF XSEDE](<https://portal.xsede.org/resource-monitor>) sites acquired as part of the [Campus Champions](<https://www.xsede.org/community-engagement/campus-champions>) program. The allocation can be used for testing and benchmarking purposes by the CofC campus community. To get access to XSEDE resources, please email [me](<mailto:temelsob@cofc.edu>). <br>
<br>


# Commercial Cloud Platorms

Commercial cloud providers are a reasonable option for the right kinds of problems and workflows. They do require users to fund their own usage. Researchers who find cloud resources indispensible, but lack funding to use them can apply for educational grants.

-   Amazon AWS
     [![AWS](https://d0.awsstatic.com/logos/powered-by-aws.png)](https://aws.amazon.com/hpc/)
-   Google Cloud
-   Microsoft Azure

Amazon AWS, Microsoft Azure and Google Cloud Platform are currently the top three commercial cloud environments. They provide very similar options to draw more people into their platforms by offering limited free account for 12 months. However, Amazon AWS and Google GCP are the only ones that have a clear program to grant credits on their platforms for researchers. The application process varies, but it is safe to say that it would take months between the time of application and credits’ availability. The credits granted are limited since they are mainly intended for performing novel, proof of concept or benchmarking examples that demonstrate the capabilities of doing HPC in the cloud. Therefore, they are probably not an option for most conventional users. The research grants/credits should be thought of as a supplement rather than replacement of most researchers’ existing HPC capacity.

**Free for any use** - All three major cloud platforms provide a virtual machine for any use like hosting websites and other light operations for free for 12 months.

**Free for training and educational uses** - Amazon and Google have programs to give faculty and students accounts for training and workforce development for free. Microsoft treats its training/educational program no differently than its standard free service.

1.  Amazon - [https://aws.amazon.com/education/awseducate/](https://aws.amazon.com/education/awseducate/)
2.  Google - [https://cloud.google.com/edu/](https://cloud.google.com/edu/)
3.  Microsoft - [https://azure.microsoft.com/en-us/education/](https://azure.microsoft.com/en-us/education/)

**Grants for research computing** - Amazon and Google have programs where researchers can apply for grants in the form of credits on AWS or GCP.

AWS Cloud Credits for Research - [https://aws.amazon.com/research-credits/?refid=gs\_card](https://aws.amazon.com/research-credits/?refid=gs_card)

1.  Awarded credits vary and will be for on-demand and Spot Instance EC2 usage
2.  Submit proposal before four quarterly deadlines (March 31, June 30, September 30, and December 31.
3.  Decisions are typically communicated 2-3 months following the respective quarterly deadline)
4.  Awards are for a one-year term, and not eligible for renewal or extension

GCP Research Credits - [https://lp.google-mkto.com/gcp-research-credits-FAQ.html](https://lp.google-mkto.com/gcp-research-credits-FAQ.html)

1.  \$5000 worth GCP credits for one year
2.  Application must include a one-page proposal
3.  The applications are reviewed on a rolling basis. It takes 4-6 weeks to review proposals and 60 days to make the credits available for use
4.  \$5000 is not a lot to do much HPC for most people, but it could be enough for some faculty or a good supplement to others.

To learn more about free or inexpensive commercial cloud computing options for general purpose or HPC, please see [the synopsis here](cloud-hpc.php).
