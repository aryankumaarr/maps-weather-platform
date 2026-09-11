# AWS

No live infrastructure yet — local dev runs entirely on Docker Compose (see the root
[docker-compose.yml](../../docker-compose.yml)), so no AWS spend is required to build the
project.

## Planned free-tier-friendly shape (when we're ready to deploy)

- **Compute**: ECS Fargate (or a single free-tier `t3.micro` EC2 running Docker Compose) for
  backend + frontend.
- **Database**: RDS PostgreSQL with the `postgis` extension, `db.t3.micro`, within the AWS
  Free Tier (750 hrs/month for 12 months).
- **Cache**: ElastiCache Redis `cache.t3.micro`, or skip it initially and run Redis on the
  same instance as the app to avoid cost until traffic justifies a managed cluster.
- **Static assets / frontend**: S3 + CloudFront (both have permanent free tiers at low volume),
  or Vercel's free tier if we don't want to self-host the Next.js app.
- **Secrets**: SSM Parameter Store (free) instead of Secrets Manager (paid) for early stages.

## IaC

Not started. When we're ready, this folder should hold Terraform (open-source, free) under
`infrastructure/aws/terraform/`. Avoid AWS-specific paid add-ons (e.g. GuardDuty, paid support
plans) until there's budget and real traffic to justify them.
