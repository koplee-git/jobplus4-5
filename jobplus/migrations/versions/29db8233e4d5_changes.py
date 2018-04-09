"""changes

Revision ID: 29db8233e4d5
Revises: 
Create Date: 2018-04-08 15:18:43.837769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29db8233e4d5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('logo_url', sa.String(length=256), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('website', sa.String(length=32), nullable=True),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.Column('location', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('job',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('salary', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=256), nullable=True),
    sa.Column('condition', sa.String(length=256), nullable=True),
    sa.Column('experience', sa.String(length=256), nullable=True),
    sa.Column('degree', sa.String(length=256), nullable=True),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.Column('is_fulltime', sa.Boolean(), nullable=True),
    sa.Column('is_open', sa.Boolean(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('job_url', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('role', sa.SmallInteger(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('deliver',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.Column('company_id', sa.String(length=24), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=True),
    sa.Column('response', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['job.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('resume',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=24), nullable=True),
    sa.Column('gender', sa.String(length=24), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('college', sa.String(length=24), nullable=True),
    sa.Column('degree', sa.String(length=24), nullable=True),
    sa.Column('major', sa.String(length=24), nullable=True),
    sa.Column('work_year', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('resume')
    op.drop_table('deliver')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('job')
    op.drop_table('company')
    # ### end Alembic commands ###