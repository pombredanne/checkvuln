PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

CREATE TABLE ports (
    id INTEGER PRIMARY KEY,
    name TEXT COLLATE NOCASE,
    portfile TEXT,
    url TEXT,
    location TEXT,
    epoch INTEGER,
    version TEXT COLLATE VERSION,
    revision INTEGER,
    variants TEXT,
    negated_variants TEXT,
    state TEXT,
    date DATETIME,
    installtype TEXT,
    archs TEXT,
    requested INT,
    os_platform TEXT,
    os_major INTEGER,
    UNIQUE (name, epoch, version, revision, variants),
    UNIQUE (url, epoch, version, revision, variants)
);

INSERT INTO "ports" VALUES(
    1,                      /* id */
    'libxml2',              /* name */
    'portfile',             /* portfile */
    NULL,                   /* url */
    'location.tbz2',        /* location */
    0,                      /* epoch */
    '2.9.2',                /* version */
    2,                      /* revision */
    '',                     /* variants */
    '',                     /* negated_variants */
    'installed',            /* state */
    0,                      /* date */
    'image',                /* installtype */
    'x86_64',               /* archs */
    0,                      /* requested */
    'darwin',               /* os_platform */
    99                      /* os_major */
);

INSERT INTO "ports" VALUES(
    2,                      /* id */
    'openssl',              /* name */
    'portfile',             /* portfile */
    NULL,                   /* url */
    'location.tbz2',        /* location */
    0,                      /* epoch */
    '1.0.2',                /* version */
    0,                      /* revision */
    '',                     /* variants */
    '',                     /* negated_variants */
    'installed',            /* state */
    0,                      /* date */
    'image',                /* installtype */
    'x86_64',               /* archs */
    0,                      /* requested */
    'darwin',               /* os_platform */
    99                      /* os_major */
);

INSERT INTO "ports" VALUES(
    3,                      /* id */
    'openvpn2',             /* name */
    'portfile',             /* portfile */
    NULL,                   /* url */
    'location.tbz2',        /* location */
    0,                      /* epoch */
    '2.3.4',                /* version */
    0,                      /* revision */
    '',                     /* variants */
    '',                     /* negated_variants */
    'installed',            /* state */
    0,                      /* date */
    'image',                /* installtype */
    'x86_64',               /* archs */
    1,                      /* requested */
    'darwin',               /* os_platform */
    99                      /* os_major */
);

INSERT INTO "ports" VALUES(
    4,                      /* id */
    'sqlite3',              /* name */
    'portfile',             /* portfile */
    NULL,                   /* url */
    'location.tbz2',        /* location */
    0,                      /* epoch */
    '3.8.8.3',              /* version */
    0,                      /* revision */
    '',                     /* variants */
    '',                     /* negated_variants */
    'installed',            /* state */
    0,                      /* date */
    'image',                /* installtype */
    'x86_64',               /* archs */
    0,                      /* requested */
    'darwin',               /* os_platform */
    99                      /* os_major */
);

INSERT INTO "ports" VALUES(
    5,                      /* id */
    'python27',             /* name */
    'portfile',             /* portfile */
    NULL,                   /* url */
    'location.tbz2',        /* location */
    0,                      /* epoch */
    '2.7.6',                /* version */
    3,                      /* revision */
    '',                     /* variants */
    '',                     /* negated_variants */
    'installed',            /* state */
    0,                      /* date */
    'image',                /* installtype */
    'x86_64',               /* archs */
    1,                      /* requested */
    'darwin',               /* os_platform */
    99                      /* os_major */
);

INSERT INTO "ports" VALUES(
    6,                      /* id */
    'curl',                 /* name */
    'portfile',             /* portfile */
    NULL,                   /* url */
    'location.tbz2',        /* location */
    0,                      /* epoch */
    '7.44.0',               /* version */
    0,                      /* revision */
    '',                     /* variants */
    '',                     /* negated_variants */
    'installed',            /* state */
    0,                      /* date */
    'image',                /* installtype */
    'x86_64',               /* archs */
    1,                      /* requested */
    'darwin',               /* os_platform */
    99                      /* os_major */
);

INSERT INTO "ports" VALUES(
    7,                      /* id */
    'bzip2',                /* name */
    'portfile',             /* portfile */
    NULL,                   /* url */
    'location.tbz2',        /* location */
    0,                      /* epoch */
    '1.0.6',                /* version */
    0,                      /* revision */
    '',                     /* variants */
    '',                     /* negated_variants */
    'installed',            /* state */
    0,                      /* date */
    'image',                /* installtype */
    'x86_64',               /* archs */
    0,                      /* requested */
    'darwin',               /* os_platform */
    99                      /* os_major */
);

INSERT INTO "ports" VALUES(
    8,                      /* id */
    'lzo2',                 /* name */
    'portfile',             /* portfile */
    NULL,                   /* url */
    'location.tbz2',        /* location */
    0,                      /* epoch */
    '2.09',                 /* version */
    0,                      /* revision */
    '',                     /* variants */
    '',                     /* negated_variants */
    'installed',            /* state */
    0,                      /* date */
    'image',                /* installtype */
    'x86_64',               /* archs */
    0,                      /* requested */
    'darwin',               /* os_platform */
    99                      /* os_major */
);

INSERT INTO "ports" VALUES(
    9,                      /* id */
    'db48',                 /* name */
    'portfile',             /* portfile */
    NULL,                   /* url */
    'location.tbz2',        /* location */
    0,                      /* epoch */
    '4.8.30',               /* version */
    4,                      /* revision */
    '',                     /* variants */
    '',                     /* negated_variants */
    'installed',            /* state */
    0,                      /* date */
    'image',                /* installtype */
    'x86_64',               /* archs */
    0,                      /* requested */
    'darwin',               /* os_platform */
    99                      /* os_major */
);

INSERT INTO "ports" VALUES(
    10,                     /* id */
    'apache2',              /* name */
    'portfile',             /* portfile */
    NULL,                   /* url */
    'location.tbz2',        /* location */
    0,                      /* epoch */
    '2.2.31',               /* version */
    0,                      /* revision */
    '',                     /* variants */
    '',                     /* negated_variants */
    'installed',            /* state */
    0,                      /* date */
    'image',                /* installtype */
    'x86_64',               /* archs */
    1,                      /* requested */
    'darwin',               /* os_platform */
    99                      /* os_major */
);

INSERT INTO "ports" VALUES(
    11,                     /* id */
    'apache24-devel',       /* name */
    'portfile',             /* portfile */
    NULL,                   /* url */
    'location.tbz2',        /* location */
    0,                      /* epoch */
    '2.4.16',               /* version */
    0,                      /* revision */
    '',                     /* variants */
    '',                     /* negated_variants */
    'installed',            /* state */
    0,                      /* date */
    'image',                /* installtype */
    'x86_64',               /* archs */
    1,                      /* requested */
    'darwin',               /* os_platform */
    99                      /* os_major */
);

INSERT INTO "ports" VALUES(
    12,                     /* id */
    'openssh',              /* name */
    'portfile',             /* portfile */
    NULL,                   /* url */
    'location.tbz2',        /* location */
    0,                      /* epoch */
    '6.9p1',                /* version */
    2,                      /* revision */
    '',                     /* variants */
    '',                     /* negated_variants */
    'installed',            /* state */
    0,                      /* date */
    'image',                /* installtype */
    'x86_64',               /* archs */
    1,                      /* requested */
    'darwin',               /* os_platform */
    99                      /* os_major */
);

INSERT INTO "ports" VALUES(
    13,                     /* id */
    'rb19-rails',           /* name */
    'portfile',             /* portfile */
    NULL,                   /* url */
    'location.tbz2',        /* location */
    0,                      /* epoch */
    '3.0.5',                /* version */
    0,                      /* revision */
    '',                     /* variants */
    '',                     /* negated_variants */
    'installed',            /* state */
    0,                      /* date */
    'image',                /* installtype */
    'x86_64',               /* archs */
    1,                      /* requested */
    'darwin',               /* os_platform */
    99                      /* os_major */
);

INSERT INTO "ports" VALUES(
    14,                     /* id */
    'rb-rails',             /* name */
    'portfile',             /* portfile */
    NULL,                   /* url */
    'location.tbz2',        /* location */
    0,                      /* epoch */
    '2.3.5',                /* version */
    0,                      /* revision */
    '',                     /* variants */
    '',                     /* negated_variants */
    'installed',            /* state */
    0,                      /* date */
    'image',                /* installtype */
    'x86_64',               /* archs */
    1,                      /* requested */
    'darwin',               /* os_platform */
    99                      /* os_major */
);

INSERT INTO "ports" VALUES(
    15,                     /* id */
    'nodejs',               /* name */
    'portfile',             /* portfile */
    NULL,                   /* url */
    'location.tbz2',        /* location */
    0,                      /* epoch */
    '0.12.7',               /* version */
    0,                      /* revision */
    '',                     /* variants */
    '',                     /* negated_variants */
    'installed',            /* state */
    0,                      /* date */
    'image',                /* installtype */
    'x86_64',               /* archs */
    1,                      /* requested */
    'darwin',               /* os_platform */
    99                      /* os_major */
);

INSERT INTO "ports" VALUES(
    16,                     /* id */
    'nodejs-devel',         /* name */
    'portfile',             /* portfile */
    NULL,                   /* url */
    'location.tbz2',        /* location */
    0,                      /* epoch */
    '4.1.2',                /* version */
    0,                      /* revision */
    '',                     /* variants */
    '',                     /* negated_variants */
    'installed',            /* state */
    0,                      /* date */
    'image',                /* installtype */
    'x86_64',               /* archs */
    1,                      /* requested */
    'darwin',               /* os_platform */
    99                      /* os_major */
);

INSERT INTO "ports" VALUES(
    17,                     /* id */
    'leafnode',             /* name */
    'portfile',             /* portfile */
    NULL,                   /* url */
    'location.tbz2',        /* location */
    0,                      /* epoch */
    '1.11.8',               /* version */
    0,                      /* revision */
    '',                     /* variants */
    '',                     /* negated_variants */
    'installed',            /* state */
    0,                      /* date */
    'image',                /* installtype */
    'x86_64',               /* archs */
    0,                      /* requested */
    'darwin',               /* os_platform */
    99                      /* os_major */
);

INSERT INTO "ports" VALUES(
    18,                     /* id */
    'gnupg21',              /* name */
    'portfile',             /* portfile */
    NULL,                   /* url */
    'location.tbz2',        /* location */
    0,                      /* epoch */
    '2.1.8',                /* version */
    0,                      /* revision */
    '',                     /* variants */
    '',                     /* negated_variants */
    'installed',            /* state */
    0,                      /* date */
    'image',                /* installtype */
    'x86_64',               /* archs */
    1,                      /* requested */
    'darwin',               /* os_platform */
    99                      /* os_major */
);

INSERT INTO "ports" VALUES(
    19,                     /* id */
    'gnupg2',               /* name */
    'portfile',             /* portfile */
    NULL,                   /* url */
    'location.tbz2',        /* location */
    0,                      /* epoch */
    '2.0.28',               /* version */
    0,                      /* revision */
    '',                     /* variants */
    '',                     /* negated_variants */
    'installed',            /* state */
    0,                      /* date */
    'image',                /* installtype */
    'x86_64',               /* archs */
    1,                      /* requested */
    'darwin',               /* os_platform */
    99                      /* os_major */
);

INSERT INTO "ports" VALUES(
    20,                     /* id */
    'nginx',                /* name */
    'portfile',             /* portfile */
    NULL,                   /* url */
    'location.tbz2',        /* location */
    0,                      /* epoch */
    '1.9.5',                /* version */
    0,                      /* revision */
    '',                     /* variants */
    '',                     /* negated_variants */
    'installed',            /* state */
    0,                      /* date */
    'image',                /* installtype */
    'x86_64',               /* archs */
    1,                      /* requested */
    'darwin',               /* os_platform */
    99                      /* os_major */
);

COMMIT;
