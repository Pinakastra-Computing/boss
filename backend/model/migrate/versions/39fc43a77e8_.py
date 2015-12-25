"""Added Time State table

Revision ID: 39fc43a77e8
Revises: 1e05d3e1d36
Create Date: 2015-08-06 17:16:47.292141

"""

# revision identifiers, used by Alembic.
revision = '39fc43a77e8'
down_revision = '1e05d3e1d36'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_account():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('time_state',
    sa.Column('time_state_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('scheduled_at', sa.DateTime(), nullable=False),
    sa.Column('action', sa.String(length=64), nullable=False),
    sa.Column('step', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.customer_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('time_state_id'),
    sa.UniqueConstraint('customer_id', 'name')
    )
    op.create_index(op.f('ix_time_state_scheduled_at'), 'time_state', ['scheduled_at'], unique=False)
    ### end Alembic commands ###


def downgrade_account():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_time_state_scheduled_at'), table_name='time_state')
    op.drop_table('time_state')
    ### end Alembic commands ###


def upgrade_fitter():
    pass


def downgrade_fitter():
    pass

