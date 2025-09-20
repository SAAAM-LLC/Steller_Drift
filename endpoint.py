from flask import Flask, jsonify, request
from saAam_core.core.consciousness_core import ConsciousnessCore
from saAam_core.core.advanced_world_systems import DynamicWorldSystem

app = Flask(__name__)

# Initialize world and entities
world = DynamicWorldSystem()
entities = {id: ConsciousnessCore() for id in range(100)}  # Example: 100 entities

@app.route('/update', methods=['POST'])
def update_world():
    """Update all entities and the world."""
    try:
        dt = request.json.get('dt', 0.016)

        # Update entities
        for entity_id, core in entities.items():
            world_state = world.get_state(entity_id)
            core.update(dt=dt, world_state=world_state)

        # Update the world system
        world.update(dt=dt)

        return jsonify({'status': 'success'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/state/<int:entity_id>', methods=['GET'])
def get_entity_state(entity_id):
    """Fetch the current state of an entity."""
    if entity_id not in entities:
        return jsonify({'error': 'Entity not found'}), 404

    state = entities[entity_id].to_dict()  # Serialize the entity state
    return jsonify(state), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
