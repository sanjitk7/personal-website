# Shared content for all redesign mockups (condensed from index.html).
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent

def seo_head():
    """Exact <head> SEO block from the live index.html (meta, OG, JSON-LD, gtag), minus the old stylesheet."""
    s = (ROOT/'index.html').read_text()
    head = s[s.index('<head>')+6:s.index('</head>')]
    head = head.replace('<link rel="stylesheet" type="text/css" href="stylesheet.css">', '')
    head = head.replace('href="images/', 'href="../images/')
    return head.strip()

INTRO = ("I'm a software engineer at Amazon Music in Seattle, working on subscription growth across voice and mobile. "
         "I hold a master's in computer science from the University of Illinois Urbana-Champaign, and I'm broadly "
         "interested in full stack development and distributed, networked systems.")
INTRO_SHORT = "Software engineer at Amazon Music in Seattle. Master's degree in Computer Science from UIUC. I build full stack products and distributed systems."
OUTSIDE = "Outside of work: road bike, camera in hand, hunting for a new coffee shop to read a book at."

LINKS = [
    ("Email", "mailto:sanjitk2018@gmail.com"),
    ("Resume", "../data/SanjitKumarResume_FullStack.pdf"),
    ("LinkedIn", "https://www.linkedin.com/in/sanjitk7/"),
    ("GitHub", "https://github.com/sanjitk7/"),
    ("Photography", "https://vsco.co/sanjitk7/gallery"),
]
VSCO = "https://vsco.co/sanjitk7/gallery"

EXPERIENCE = [
    dict(role="Software Development Engineer", org="Amazon Music", url="https://music.amazon.com",
         dates="Sep 2024 – Present", start="2024", place="Seattle, WA", logo="amz.png",
         summary="Experimental upsell experiences via proactive voice notifications at scale, plus Android upsell and engagement work.",
         metric="150k+ annualized tier signups", metric_sentence="Together these helped drive 150k+ annualized tier signups."),
    dict(role="Graduate TA, Distributed Systems", org="UIUC Computer Science", url="https://cs.illinois.edu",
         dates="Jan – May 2024", start="2024", place="Champaign, IL", logo="uofilogoblue2.jpeg",
         summary="CS425 with Prof. Radhika Mittal. Mentored students building multicast, distributed transactions, Raft and a distributed file system.",
         metric=None),
    dict(role="Software Engineer Intern", org="Aviz Networks", url="https://www.aviznetworks.com",
         dates="May – Nov 2023", start="2023", place="San Jose, CA", logo="aviz-logo-transparent.webp",
         summary="Built a core ONE-DL feature streaming data-center packet metadata to the cloud with Kafka, Elasticsearch and Redis, tuned with batching and DPDK kernel bypass.",
         metric="3× throughput, 50% lower latency", metric_sentence="Reached 3× throughput and 50% lower latency."),
    dict(role="Full Stack Developer Intern", org="WebKnot Technologies", url="https://webknot.in",
         dates="Nov – Dec 2020", start="2020", place="Bangalore, India", logo="webknot-logo-purple.png",
         summary="React UIs and Node/Express APIs for two MERN apps; integrated TensorFlow object detection with the Shinobi CCTV framework.",
         metric=None),
]

PROJECTS = [
    dict(name="IDunno", short="Systems", tag="Distributed systems", url="https://github.com/sanjitk7/cs425-distributed-systems/tree/master/MP4",
         line="A distributed ML inference scheduler on 10 Linux VMs, built from scratch.",
         more="Java and Python. Real-time scheduling to optimize query rate for ResNet/ImageNet tasks, with its own logging service, group membership and failure detector, and distributed file system.",
         img="idunno-1.png", img_hover="idunno-2.png", stack=["Java","Python"], featured=True),
    dict(name="Linux kernel modules", short="Kernels", tag="Operating systems", url="https://github.com/sanjitk7/linux-kernel-modules/tree/master",
         line="A page fault profiler, a rate-monotonic scheduler and a CPU time tracker as kernel modules.",
         more="Virtual page fault profiling at 20 samples/sec via a delayed work queue; an RMS real-time scheduler for single-core CPUs; process CPU time via workqueues and timers, all over the proc filesystem.",
         img="osd_mp1.png", img_hover="osd_mp3.png", stack=["C","Linux"], featured=True),
    dict(name="Interactive computer graphics", short="Graphics", tag="Graphics", url="https://graphics-projects.sanjitkumar.me/",
         line="A rasterizer and ray tracer from scratch, plus WebGL terrain, flight and particle simulations.",
         more="Procedural terrain via random faults, diffuse/specular lighting, erosion, a flight sim over it, and particles under momentum, gravity and drag.",
         img="webgl-6.png", img_hover="webgl-3-1.png", stack=["WebGL","JS"], featured=True),
    dict(name="Data systems & ML", short="Data", tag="Data systems", url="https://github.com/sanjitk7/data-systems-projects",
         line="Online aggregation, HyperLogLog, a Parquet ASCII encoder in Apache Arrow, and Flatbuffers over shared memory.",
         more="Progressive approximate answers for Pandas queries; cardinality estimation; a new Arrow/Parquet encoder; zero-copy DataFrame sharing between sessions.",
         img="flatbuffers.png", stack=["C++","Python"], featured=False),
    dict(name="RealWorldBugDiscovery", short="Testing", tag="Software testing", url="https://youtu.be/3ebt6BfSug0",
         line="Benchmarking real-world bugs from Defects4J, BugSwarm, Bears and QuixBugs against Randoop and EvoSuite.",
         more="Coverage via Clover, IntelliJ and JaCoCo, then suspiciousness scores to localize likely faulty lines.",
         img="fault-localization-mbfl.png", stack=["Java"], featured=False),
    dict(name="WildSprint", short="Hackathon", tag="Hackathon winner", url="https://github.com/ambur-biryani/wild-sprint-frontend",
         line="ETH-powered fundraising for wildlife sanctuaries with live streams. Two awards at DevSpace '21.",
         more="Best Ethereum Powered Project and Best Dyte Powered Project at DevSpace '21 (CSI, VIT).",
         img="wild-sprint-1.png", stack=["Ethereum","React"], featured=False),
    dict(name="KYYarn", short="Web", tag="Full stack", url="https://github.com/sanjitk7/KYYarnTrader",
         line="A MERN catalogue and BI dashboard for a yarn trading company in Erode, India.",
         more="Collects business inquiries and turns them into visualizations; also an alternative JavaFX frontend.",
         img="ky-1.png", stack=["MERN","JavaFX"], featured=False),
    dict(name="DockerMapReduce", short="Systems", tag="Distributed systems", url="https://github.com/sanjitk7/MapReducePython",
         line="MapReduce word counts across Docker containers acting as map and reduce nodes.",
         more="Throughput measured while scaling data and nodes up and down.",
         img="mapred-1.png", stack=["Python","Docker"], featured=False),
]

PUBLICATION = dict(title="A Survey on Internet of Things Security: Attacks, Solutions, Strengths and Limitations",
    venue="AIMV 2021", url="https://ieeexplore.ieee.org/document/9670971")

# Simple monochrome line icons (24x24, stroke=currentColor) for the compact project list.
ICONS = {
 "Data systems & ML": '<ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v6c0 1.7 3.6 3 8 3s8-1.3 8-3V5"/><path d="M4 11v6c0 1.7 3.6 3 8 3s8-1.3 8-3v-6"/>',
 "RealWorldBugDiscovery": '<rect x="7" y="7" width="10" height="13" rx="5"/><path d="M12 11v9M7 12H3M21 12h-4M7 17H4M20 17h-3M9 7l-2-3M15 7l2-3"/>',
 "WildSprint": '<path d="M11 20A7 7 0 0 1 4 13c0-5 4-9 16-9 0 12-4 16-9 16z"/><path d="M4 20c4-4 7-7 11-10"/>',
 "KYYarn": '<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/>',
 "DockerMapReduce": '<path d="M12 2l9 5-9 5-9-5 9-5z"/><path d="M3 12l9 5 9-5"/><path d="M3 17l9 5 9-5"/>',
}
