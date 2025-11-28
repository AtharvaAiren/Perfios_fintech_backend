"""initial

Revision ID: 0001_initial
Revises: 
Create Date: 2025-01-01 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = '0001_initial'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )
    op.create_table('farmers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('aadhaar', sa.String(), nullable=True),
        sa.Column('pan', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )
    op.create_table('consents',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('farmer_id', sa.Integer(), sa.ForeignKey('farmers.id'), nullable=False),
        sa.Column('purpose', sa.String(), nullable=False),
        sa.Column('scope', sa.JSON(), nullable=True),
        sa.Column('granted', sa.Boolean(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )
    op.create_table('applications',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('farmer_id', sa.Integer(), sa.ForeignKey('farmers.id'), nullable=False),
        sa.Column('product', sa.String(), nullable=False),
        sa.Column('status', sa.String(), nullable=True),
        sa.Column('result', sa.JSON(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )
    op.create_table('perfios_results',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('raw', sa.JSON(), nullable=False),
        sa.Column('summary', sa.JSON(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )
    op.create_table('bank_statements',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('farmer_id', sa.Integer(), sa.ForeignKey('farmers.id'), nullable=False),
        sa.Column('file_path', sa.String(), nullable=False),
        sa.Column('uploaded_at', sa.DateTime(), nullable=True),
        sa.Column('perfios_result_id', sa.Integer(), sa.ForeignKey('perfios_results.id'), nullable=True),
    )
    op.create_table('onevigil_results',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('farmer_id', sa.Integer(), sa.ForeignKey('farmers.id'), nullable=False),
        sa.Column('raw', sa.JSON(), nullable=False),
        sa.Column('score', sa.Float(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )
    op.create_table('risk_results',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('application_id', sa.Integer(), sa.ForeignKey('applications.id'), nullable=False),
        sa.Column('perfios_id', sa.Integer(), sa.ForeignKey('perfios_results.id'), nullable=True),
        sa.Column('onevigil_id', sa.Integer(), sa.ForeignKey('onevigil_results.id'), nullable=True),
        sa.Column('combined_score', sa.Float(), nullable=True),
        sa.Column('details', sa.JSON(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
    )

def downgrade():
    op.drop_table('risk_results')
    op.drop_table('onevigil_results')
    op.drop_table('bank_statements')
    op.drop_table('perfios_results')
    op.drop_table('applications')
    op.drop_table('consents')
    op.drop_table('farmers')
    op.drop_table('users')
